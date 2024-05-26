from rest_framework import serializers
from .models import User, Content, Media, Model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name', 'password_hash', 'email', 'avatar_url', 'registration_time', 'update_time']


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['content_id', 'title', 'category', 'content_text']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['image_id', 'user', 'file_type', 'file_url', 'upload_time']


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ['model_id', 'user', 'model_path', 'model_description', 'created_at', 'images']
