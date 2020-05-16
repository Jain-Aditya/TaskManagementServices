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

# Create a Task
- POST http://127.0.0.1:8000/create-task/
- User should be authenticated to access this API.
- For clients to authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed   by the string literal "Token", with whitespace separating the two strings. For example:

`Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b`

- The input data should be JSON with keys `task_description`, `due_date`, `label` and `status`
- For example:
- `{
	"task_description": "This is a test task",
	"due_date": "2020-12-12",
	"label": "personal",
	"status": "done"
}`

# Retrieve all tasks
- GET http://127.0.0.1:8000/all_tasks/
- User should be authenticated to access this API. (Same as the above API)
