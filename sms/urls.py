# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('new-msg/', views.notification, name='notification'),
    path('send-msg/', views.send_msg, name='send_msg'),
]
