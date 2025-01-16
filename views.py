from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .models import Message
from django.contrib.auth.models import User

def home(request):
    users = User.objects.exclude(username=request.user.username)  # Exclude the current user
    return render(request, 'chat/home.html', {'users': users})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def chat_room(request, room_name):
    messages = Message.objects.filter(sender__username=room_name) | Message.objects.filter(recipient__username=room_name)
    messages = messages.order_by('timestamp')
    return render(request, 'chat/chat_room.html', {'room_name': room_name, 'messages': messages})
