from json import JSONDecodeError

from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .models import User, Content, Media, Model, Comment
from .serializer import UserSerializer, ContentSerializer, MediaSerializer, ModelSerializer
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
import json
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone

import sys
# 将项目根目录添加到 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from inferModel.infer2 import predict




def index(request):
    return HttpResponse("<h1>Hello world<h1>")


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            email = data.get('email')
            password = data.get('password')
            if email and password:
                try:
                    user = User.objects.get(email=email)
                    if check_password(password, user.password_hash):
                        user_data = {
                            'user_id': user.user_id,
                            'user_name': user.user_name,
                            'email': user.email,
                            'avatar_url': user.avatar_url,
                            'registration_time': user.registration_time,
                            'update_time': user.update_time,
                        }
                        return JsonResponse(user_data, status=200)
                    else:
                        return JsonResponse({"error": "密码错误"}, status=401)
                except User.DoesNotExist:
                    return JsonResponse({"error": "该用户未注册"}, status=401)
            else:
                return JsonResponse({"error": "必须填写邮箱和密码"}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({"error": "无效的JSON"}, status=400)

    return JsonResponse({"error": "无效的请求方法"}, status=405)


@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            email = data.get('email')
            password = data.get('password')

            if not name or not email or not password:
                return JsonResponse({"error": "请填写所有字段并同意用户协议"}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "该邮箱已被注册"}, status=400)

            hashed_password = make_password(password)
            avatar_url = 'default_avatar.jpg'
            user = User(user_name=name, email=email, password_hash=hashed_password, avatar_url=avatar_url)
            user.save()

            return JsonResponse({"message": "用户注册成功"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "无效的JSON"}, status=400)

    return JsonResponse({"error": "无效的请求方法"}, status=405)


@csrf_exempt
def get_message(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                name = user.user_name
                avatar_url = user.avatar_url
                user_id = user.user_id
                return JsonResponse({'name': name, 'avatar_url': avatar_url, 'user_id':user_id}, status=200)

            except User.DoesNotExist:
                return JsonResponse({"error": "查找的数据不存在"}, status=401)

        else:
            return JsonResponse({"error": "email参数不存在"}, status=400)

    return JsonResponse({"error": "无效的请求方法"}, status=405)


@csrf_exempt
def infer_view(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                photo_url = user.photo_url
                top1_pro, top2_pro, top3_pro, top1_res, top2_res, top3_res = predict(photo_url)

                return JsonResponse({'top1_pro': top1_pro, 'top2_pro': top2_pro, 'top3_pro': top3_pro,
                                     'top1_res': top1_res, 'top2_res': top2_res, 'top3_res': top3_res}, status=200)
                # return JsonResponse({'email': email}, status=200)

            except User.DoesNotExist:
                return JsonResponse({"error": "查找的数据不存在"}, status=401)
        else:
            return JsonResponse({"error": "email参数不存在"}, status=400)
    return JsonResponse({"error": "无效的请求方法"}, status=405)

@csrf_exempt
def account_view(request):
    print(request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            email = data.get('email')
            try:
                user = User.objects.get(email=email)
                user.user_name = name
                user.update_time = timezone.now()
                user.save()
                return JsonResponse({"message": "更新成功"}, status=201)

            except User.DoesNotExist:
                return JsonResponse({"error": "查找的数据不存在"}, status=401)

        except JSONDecodeError:
            JsonResponse({"error": "无效的JSON"}, status=400)

    return JsonResponse({"error": "无效的请求方法"}, status=405)


@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_path = os.path.join(settings.BASE_DIR, 'images', image.name)

        if not os.path.exists(os.path.dirname(image_path)):
            try:
                os.makedirs(os.path.dirname(image_path))
            except OSError as e:
                return JsonResponse({'error': 'Failed to create directory: ' + str(e)}, status=500)
                # 如果文件存在，则删除原文件
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except OSError as e:
                return JsonResponse({'error': 'Failed to delete existing file: ' + str(e)}, status=500)

        path = default_storage.save(image_path, ContentFile(image.read()))
        return JsonResponse({'message': 'Image uploaded successfully', 'path': path}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def upload_avatar(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        file = request.FILES['file']

        user = User.objects.get(email=email)
        user.avatar_url = str(user.user_id) + '.jpg'
        print(user.avatar_url)
        user.update_time = timezone.now()
        user.save()
        file_name = user.avatar_url
        file_path = os.path.join('images', file_name)

        if default_storage.exists(file_path):
            default_storage.delete(file_path)

        file_path = default_storage.save(file_path, ContentFile(file.read()))

        return JsonResponse({'message': 'Avatar uploaded successfully', 'file_path': file_path})
    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def get_image(request):
    if request.method == 'GET':
        image_name = request.GET.get('image_name')
        if image_name:
            image_path = os.path.join(settings.BASE_DIR, 'images', image_name)
            if os.path.exists(image_path):
                with open(image_path, 'rb') as img_file:
                    return HttpResponse(img_file.read(), content_type="image/png")
            else:
                return JsonResponse({'error': 'Image not found'}, status=404)
        else:
            return JsonResponse({'error': 'Image name not provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


# 获取所有用户 头像、昵称、分数
def userInfo(request):
    users = User.objects.all().order_by('-score').values('user_name', 'score', 'avatar_url')  # 使用values来获取指定字段
    data = list(users)  # 将QuerySet转换为列表
    # print(data)
    return JsonResponse(data, safe=False)  # 返回JSON响应


# 根据传入的参数 email 检索出用户信息
def get_user_info_by_email(request, email):
    try:
        # 假设UserProfile模型有一个email字段，并且它是唯一的
        user_profile = User.objects.get(email=email)
        user_info = {
            'user_name': user_profile.user_name,
            'score': user_profile.score,
            'avatar_url': user_profile.avatar_url,
        }
        return JsonResponse(user_info, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404, safe=False)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer



