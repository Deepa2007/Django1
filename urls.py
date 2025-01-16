from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]
