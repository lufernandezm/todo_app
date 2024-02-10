# Task Manager Application

This is a simple command-line based Task Manager application written in Python. It uses the typer library for creating a beautiful command-line interface.

## Features

1. Add a new task.
2. List all tasks.
3. Mark a task as completed.
4. Exit the application.

## Installation

This application uses a virtual environment for managing dependencies. Follow these steps to set up and run the application:

1. Clone the repository to your local machine.

2. Navigate to the project directory and create a virtual environment:


## Prerequisites

Before you begin, ensure you have Python 3.8 or higher installed on your machine. You can verify your Python version by running:

#### ` python --version`

### Setting Up the Development Environment

1. Create a new Virtual Environment
    #### ` python -m venv venv `

2. Activate the Virtual Environment

- On Windows:
    #### ` .\venv\Scripts\activate`

- On macOS and Linux:
    #### ` source venv/bin/activate`

You should now see (venv) before your command prompt, indicating that the virtual environment is active.

3. Install Dependencies

Before installing dependencies, navigate to the app directory where the application is located:

#### ` cd app`

Then run:
#### ` pip install -r requirements.txt`

### Running the Application

Before running the Application, make sure you are in app/ directory:

To run the  application, use the following command:
#### ` python main.py`