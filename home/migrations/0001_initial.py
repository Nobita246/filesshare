# Generated by Django 3.2.12 on 2023-06-11 17:01

from django.db import migrations, models
import django.db.models.deletion
import home.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FolderFiles',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now=True)),
                ('file', models.FileField(upload_to=home.models.get_file_folder)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.folder')),
            ],
        ),
    ]
