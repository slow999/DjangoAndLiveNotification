# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('new-msg/', views.index, name='send-msg'),
    path('send-msg/', views.new_message, name='new-msg'),
]
