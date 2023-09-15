# flask_login_using_mongo

Test Api with Postman

![Screenshot (130)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/31896285-e98e-45cc-a673-b6969a0df175)

![Screenshot (131)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/08abc44f-bb51-4f01-a6c9-fa3c4749159e)


Create & Read
![Screenshot (124)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/aeb4e0a0-3cb5-4683-927f-f166f3b7ddfb)

![Screenshot (125)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/3b8a448d-7724-4d5c-b60f-4c17f1739f06)


Update

![Screenshot (125)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/062f1e6d-7968-4c54-9937-26afff958be4)

![Screenshot (127)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/4f2eee72-e39a-4a5b-aa22-4fe4a907896a)


Delete
![Screenshot (128)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/9bec5c28-00d1-4521-a507-cef989f40ab5)

![Screenshot (129)](https://github.com/Hari-durai/flask_login_using_mongo/assets/91016875/60ee27aa-8029-4eb5-a1cf-1e4645965e3f)


 

```markdown
# Flask Login App with MongoDB Testing Api  with postman

This is a simple Flask web application that demonstrates user authentication and login functionality using MongoDB as the database. Users can register, log in.

## Features

- User registration with password hashing

- MongoDB as the database to store user information

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10 installed on your system.
- MongoDB installed and running locally or on a remote server.
- Basic knowledge of Flask and MongoDB.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hari-durai/flask_login_using_mongo.git
   ```



2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required Python packages:

   ```bash
   pip install flask
   pip install pymongo
   ```
## configuration
 1. create account in mongodb
 2. create database
 3. add network access like ip address
 4. create python drive and get the uri
 5. Replace password with  password you mention  in the network access

## Usage

1. Start the Flask application:

   ```bash
   flask run
   ```

2. Access the app in your web browser at `http://localhost:5000`.

## Directory Structure

The project directory structure looks like this:

```
flask-login-mongodb/
│
├── app/
│   ├── app.py
│   ├── mongo.py
│   └── templates/
│       ├── index.html
│       ├── result.html
│    
│

```

- `app/` contains the Flask application code.
- `instance/` contains configuration files, including `config.py` for sensitive data (not committed to version control).
- `.env` stores environment variables (not committed to version control).
- `run.py` is the entry point to run the Flask app.

