from rest_framework import serializers
from .models import Folder, FolderFiles
import shutil


class FilesSerializer(serializers.Serializer):
    files = serializers.ListField(
        child=serializers.FileField(max_length=100000000)
    )
    folder = serializers.CharField(required=False)

    def make_zip(self, folder):
        shutil.make_archive(
            f'public/media/zip/{folder}', 'zip', f'public/media/{folder}')

    def create(self, validated_data):
        files = validated_data.pop('files')
        folder_obj = Folder.objects.create()
        for file in files:
            file_obj = FolderFiles.objects.create(folder=folder_obj, file=file)

        self.make_zip(str(folder_obj.uid))

        return {"folder": str(folder_obj.uid), "files": {}}
