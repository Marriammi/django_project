# ✨ Project

This project is a simple Django API that responds with the text "Hello World 6" to a request for the appropriate URL path.

## 🔨 Install

1. **Clone the Repository:**

   ```bash
    git clone https://github.com/Marriammi/django_project.git
    cd .\first\
   ```

2. **Create a virtual environment to install dependencies in and activate it:**

   ```bash
   virtualenv2 --no-site-packages env
   source env/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Server:**

   ```bash
   python manage.py runserver
   ```

5. **Open your browser and go to the address** http://127.0.0.1:8000

## 👀 Hello World API

To interact with the Hello World API, you can make HTTP GET requests to the following endpoint:

```http
GET /api/v1/hello-world-6
```

This API endpoint will respond with a JSON message containing the greeting.
Example of using:

    http://127.0.0.1:8000/api/v1/hello-world-6

## ❗
This example assumes that your Django development server is running locally on http://127.0.0.1:8000. Make sure to adjust the URLs accordingly if your setup is different.
