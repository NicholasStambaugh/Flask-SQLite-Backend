# Flask User Data Storage Backend
This is a simple Flask backend that allows you to store user data in a SQLite database. The backend provides two endpoints - /users to add and get users.

### Getting Started
To get started, clone the repository and install the dependencies:

```
git clone https://github.com/NicholasStambaugh/Flask-SQLite-Backend.git
cd flask-user-data-backend
pip install -r requirements.txt
```

### Usage
To start the backend, run the following command:

```
python app.py
```

The backend will be accessible at http://localhost:5000/.

### Endpoints
POST /users
This endpoint allows you to add a new user to the database. To add a user, send a POST request to /users with the following JSON payload:

```
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "secret"
}
```
### GET /users
This endpoint allows you to get a list of all users in the database. To get a list of users, send a GET request to /users.

### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### License
MIT
