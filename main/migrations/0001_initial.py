# Generated by Django 5.0.6 on 2024-05-23 20:49

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('category', models.CharField(db_index=True, max_length=100)),
                ('content_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True)),
                ('avatar_url', models.URLField(blank=True, max_length=255, null=True)),
                ('registration_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_path', models.CharField(max_length=255)),
                ('model_description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('images', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('file_type', models.CharField(max_length=50)),
                ('file_url', models.URLField(max_length=255)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
