from django.db import models
import uuid
import os

# Create your models here.


class Folder(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)


def get_file_folder(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)


class FolderFiles(models.Model):
    uid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateField(auto_now=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_file_folder)
