# Django1
#Step 1: Set up the Django Project
Install Django and Channels First, you'll need to install Django, Django Channels (for WebSocket support), and Redis (for managing WebSocket connections).

pip install django channels channels_redis

Create a New Django Project Create a new Django project and a new app
django-admin startproject chat_project
cd chat_project
python manage.py startapp chat
Add Channels to Installed Apps Open the chat_project/settings.py and add channels to the INSTALLED_APPS list.

INSTALLED_APPS = [
    # other apps...
    'channels',
    'chat',
]
Configure Channels Layer Channels require a channel layer to manage communication, and Redis is the backend for this layer.

In settings.py, add:
ASGI_APPLICATION = 'chat_project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],  # Default Redis config
        },
    },
}

#Step 2: Create Models for Users and Messages
1. Create Models in chat/models.py
Add the following models for users and chat messages.

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.recipient} ({self.timestamp})"

2. Migrate the Database
After defining the models, make migrations and apply them:

python manage.py makemigrations
python manage.py migrate

Step 3: Set Up WebSocket for Real-Time Messaging
Create an ASGI Configuration File (chat_project/asgi.py)
In asgi.py, configure the application to handle WebSocket connections.

2. Create WebSocket Consumer (chat/consumers.py)
In chat/consumers.py, create the WebSocket consumer that will handle real-time communication.

3.Install Redis
If you haven't already, install Redis:
sudo apt-get install redis-server
Ensure Redis is running:
redis-server

#Step 4: Create Views, URLs, and Templates
1. Create Views for Chat and User Registration/Login in chat/views.py
2. Create URL Patterns in chat/urls.py
3. Create Templates for Home, Signup, and Chat Room

chat/templates/chat/home.html
chat/templates/chat/signup.html
chat/templates/chat/chat_room.html
Example for home.html:

#Step 5: Run the Django Application
Start Redis Server

Make sure Redis is running by executing:
redis-server
Run the Django Server

Finally, run the Django server:
python manage.py runserver
Test the Application

Visit http://127.0.0.1:8000/ in your browser to test the signup, login, chat functionality, and real-time messaging.
