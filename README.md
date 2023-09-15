# flask_login_using_mongo


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

