from django.contrib import admin
from django.urls import path
from .views import FilesAPIView

urlpatterns = [
    path('files/', FilesAPIView.as_view())
]
