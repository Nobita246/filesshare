from django.contrib import admin
from django.urls import path
from .views import FilesAPIView
from . import views

urlpatterns = [
    path('files/', FilesAPIView.as_view()),
    path('', views.home)
]
