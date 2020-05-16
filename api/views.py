from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Task
from .serializers import TaskSerializer
from datetime import date

# Create your views here.
class ListTasks(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get(self, request):
        tasks = Task.objects.filter(created_by=request.user)
        serialized = TaskSerializer(tasks, many=True)
        return Response(serialized.data)

@api_view(['POST'])
def register_user(request):
    user_instance = User(
        username = request.data['username'],
        password = request.data['password'],
        email = request.data['email']
    )
    user_instance.save()
    Token.objects.create(user=user_instance)
    token = Token.objects.get(user=user_instance)
    response_object = {
        'message': 'User created successfully',
        'username': user_instance.username ,
        'email': user_instance.email ,
        'token': token.key
    }
    return Response(response_object)

class CreateTask(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request):
        try:
            date_string = request.data['due_date']
            yy, mm , dd = list(map(int, date_string.split('-')))
            parsed_date = date(yy,mm,dd)
        except:
            return Response({'message': 'Please enter a date in yyyy-mm-dd format'})
        task_instance = Task(
            task_description = request.data['task_description'],
            due_date = parsed_date,
            label = request.data['label'],
            status = request.data['status'],
            created_by = request.user
        )
        try:
            task_instance.save()
        except:
            return Response({'message': 'Task could not be created. Please contact Aditya Jain'})
        return Response({
            'message': 'Task created successfully'
        })



