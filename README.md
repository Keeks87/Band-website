# My Django App

This is a simple Django Website.

## Building and running the app with venv

To build and run the app using venv, follow these steps:

1. Clone the repository to your local machine.
2. Create a new venv environment using the requirements.txt file:
    ```
    python3 -m venv
    source venv/scripts/activate
    pip install -r requirements.txt
    ```
3. Start the development server:
    ```
    python manage.py runserver
    ```
4. Navigate to `http://localhost:8000` in your web browser to view the site.

## Building and running the app with Docker

To build and run the app using Docker, follow these steps:

1. Clone the repository to your local machine.
2. Build the Docker image:
    ```
    docker build -t my-django-app .
    ```
3. Start the Docker container:
    ```
    docker run -p 8000:8000 my-django-app
    ```
4. Navigate to `http://localhost:8000` in your web browser to view the app...