# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_message/', views.new_message, name='new_message'),
]
