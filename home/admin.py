from django.contrib import admin
from .models import Folder, FolderFiles

# Register your models here.

admin.site.register(Folder)
admin.site.register(FolderFiles)
