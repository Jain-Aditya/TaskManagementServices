# TaskManagementServices
Task management application REST services written in django

Steps to run locally:
You should have Python3 installed on your computer

1. Run `pip3 install -r requirements.txt`. This will install all the dependencies
2. Run `Python3 manage.py makemigrations`
3. Run `Python3 manage.py migrate`
4. Run `Python3 manage.py runserver` and you would be able to access the App at `http://127.0.0.1:8000/`

# Register New user
- POST http://127.0.0.1:8000/register/
- This will require the JSON object with `username`, `password` and `email` as data.
- For example:
  `{
	"username": <username>,
	"password": <password>,
	"email": <email>
   }`
 
# Obtain auth token
- POST http://127.0.0.1:8000/api-token-auth/
- This will require JSON object whith `username` and `password` as key and will return a Token. Make sure you have already registered and the credentials are right.
- For example:
 `{
	"username": <username>,
	"password": <username>
}`
