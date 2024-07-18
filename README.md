# Todo App with Flask and SQLAlchemy

This is a simple Todo application built with Flask and SQLAlchemy.

## Features

- Add new tasks with title and description
- View existing tasks
- Edit and delete tasks
- Timestamps for task creation

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip package manager

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todo-flask-app.git

# Create a virtual environment (optional but recommended)
- python -m venv env
- source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install dependencies
- pip install -r requirements.txt

# Configure MySQL Database
- Create a MySQL database.
- Update the database connection URL in config.py:
- SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost:3306/todo_db'

# Run the application
- python app.py
- The application will start running at http://localhost:5000.

# Usage
- Register a new account or login with existing credentials.
- Add tasks using the form provided.
- Update or delete tasks using the respective buttons.

# Contributing
- Contributions are welcome! Please fork the repository and create a pull request with your improvements.

# License
- This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
- Flask
- Bootstrap
- Icons from Font Awesome

# Contact
- For issues and feature requests, please open an issue.


