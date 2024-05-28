from json import JSONDecodeError
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import subprocess
from .models import User, Content, Media, Model
from .models import User, Comment, Like
from .serializer import UserSerializer, ContentSerializer, MediaSerializer, ModelSerializer
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
import os
import random
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone
import uuid
import shutil
import sys
import base64
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_GET
from inferModel.infer2 import predict

# 将项目根目录添加到 sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
base_dir = settings.BASE_DIR

# 构建脚本的绝对路径
script_path = os.path.join(base_dir, 'voice', 'voice2.py')

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
                photo_url = os.path.join(settings.MEDIA_ROOT, 'images', f"{user.user_id}_ph.jpg")
                top1_pro, top2_pro, top3_pro, top1_res, top2_res, top3_res = predict(photo_url)

                return JsonResponse({'top1_pro': top1_pro, 'top2_pro': top2_pro, 'top3_pro': top3_pro,
                                     'top1_res': top1_res, 'top2_res': top2_res, 'top3_res': top3_res}, status=200)
            except User.DoesNotExist:
                return JsonResponse({"error": "查找的数据不存在"}, status=401)
        else:
            return JsonResponse({"error": "email参数不存在"}, status=400)
    return JsonResponse({"error": "无效的请求方法"}, status=405)

@csrf_exempt
def account_view(request):
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
            return JsonResponse({"error": "无效的JSON"}, status=400)

    return JsonResponse({"error": "无效的请求方法"}, status=405)

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        image_path = os.path.join('images', image.name)  # 相对路径，保存到MEDIA_ROOT/images目录

        full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)

        # 确保目录存在
        if not os.path.exists(os.path.dirname(full_image_path)):
            try:
                os.makedirs(os.path.dirname(full_image_path))
            except OSError as e:
                return JsonResponse({'error': 'Failed to create directory: ' + str(e)}, status=500)

        # 如果文件存在，则删除原文件
        if os.path.exists(full_image_path):
            try:
                os.remove(full_image_path)
            except OSError as e:
                return JsonResponse({'error': 'Failed to delete existing file: ' + str(e)}, status=500)

        # 保存文件到指定路径
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
        user.update_time = timezone.now()
        user.save()
        file_name = user.avatar_url
        file_path = os.path.join('images', file_name)  # 相对路径，保存到MEDIA_ROOT/images目录

        full_file_path = os.path.join(settings.MEDIA_ROOT, file_path)

        if default_storage.exists(full_file_path):
            default_storage.delete(full_file_path)

        file_path = default_storage.save(file_path, ContentFile(file.read()))

        return JsonResponse({'message': 'Avatar uploaded successfully', 'file_path': file_path})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def upload_photo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        file = request.FILES['file']

        user = User.objects.get(email=email)
        user.photo_url = str(user.user_id) + '_ph.jpg'
        user.update_time = timezone.now()
        user.save()
        file_name = user.photo_url
        file_path = os.path.join('images', file_name)

        if default_storage.exists(file_path):
            default_storage.delete(file_path)

        file_path = default_storage.save(file_path, ContentFile(file.read()))

        return JsonResponse({'message': 'Photo uploaded successfully', 'file_path': file_path})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def get_image(request):
    if request.method == 'GET':
        image_name = request.GET.get('image_name')
        if image_name:
            image_path = os.path.join('images', image_name)  # 相对路径
            full_image_path = os.path.join(settings.MEDIA_ROOT, image_path)
            if os.path.exists(full_image_path):
                with open(full_image_path, 'rb') as img_file:
                    return HttpResponse(img_file.read(), content_type="image/png")
            else:
                return JsonResponse({'error': 'Image not found'}, status=404)
        else:
            return JsonResponse({'error': 'Image name not provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def userInfo(request):
    users = User.objects.all().order_by('-score').values('user_name', 'score', 'avatar_url')  # 使用values来获取指定字段
    data = list(users)  # 将QuerySet转换为列表
    return JsonResponse(data, safe=False)  # 返回JSON响应

def get_user_info_by_email(request, email):
    try:
        user_profile = User.objects.get(email=email)
        user_info = {
            'user_name': user_profile.user_name,
            'score': user_profile.score,
            'avatar_url': user_profile.avatar_url,
        }
        return JsonResponse(user_info, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404, safe=False)

@csrf_exempt
def create_model(request):
    if request.method == 'POST':
        folder_name = str(uuid.uuid4())
        folder_path = os.path.join('images', folder_name)  # 相对路径，保存到MEDIA_ROOT/images目录

        full_folder_path = os.path.join(settings.MEDIA_ROOT, folder_path)

        if not os.path.exists(full_folder_path):
            os.makedirs(full_folder_path)

        user_id = request.POST.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status=400)

        user = get_object_or_404(User, pk=user_id)
        main_model = Model.objects.create(user=user, images=folder_path)

        return JsonResponse({'folder_url': folder_path, 'model_id': main_model.model_id}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def update_model(request):
    if request.method == 'POST':
        model_id = request.POST.get('model_id')
        model_name = request.POST.get('model_name')
        model_description = request.POST.get('model_description')

        model = get_object_or_404(Model, pk=model_id)
        model.model_name = model_name
        model.model_description = model_description

        model_folder_name = str(model.model_id)
        model_folder_path = os.path.join('models', model_folder_name)  # 相对路径，保存到MEDIA_ROOT/models目录

        full_model_folder_path = os.path.join(settings.MEDIA_ROOT, model_folder_path)

        if not os.path.exists(full_model_folder_path):
            os.makedirs(full_model_folder_path)

        model.model_path = model_folder_path
        model.save()
        return JsonResponse({'message': 'Model updated successfully', 'model_id': model.model_id}, status=200)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def upload_images(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        folder_url = request.POST.get('folder_url')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)

        images = request.FILES.getlist('images')
        if not images:
            return JsonResponse({'error': 'No images uploaded'}, status=400)

        uploaded_file_urls = []
        folder_path = os.path.join(settings.MEDIA_ROOT, folder_url)
        if not os.path.exists(folder_path):
            try:
                os.makedirs(folder_path)
            except OSError as e:
                return JsonResponse({'error': 'Failed to create directory: ' + str(e)}, status=500)

        for image in images:
            image_path = os.path.join(folder_path, image.name)

            if os.path.exists(image_path):
                try:
                    os.remove(image_path)
                except OSError as e:
                    return JsonResponse({'error': 'Failed to delete existing file: ' + str(e)}, status=500)

            path = default_storage.save(image_path, ContentFile(image.read()))
            file_url = os.path.join(settings.MEDIA_URL, folder_url, image.name)
            Media.objects.create(user=user, file_type=image.content_type, file_url=file_url)
            uploaded_file_urls.append(file_url)
        return JsonResponse({'uploaded_files': uploaded_file_urls}, status=201)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def get_image_by_path(request):
    if request.method == 'GET':
        folder_url = request.GET.get('folder_url')
        image_name = request.GET.get('image_name')
        if folder_url and image_name:
            image_path = os.path.join(settings.MEDIA_ROOT, folder_url, image_name)
            if os.path.exists(image_path):
                with open(image_path, 'rb') as img_file:
                    return HttpResponse(img_file.read(), content_type="image/jpeg")
            else:
                return JsonResponse({'error': 'Image not found'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_models(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if not user_id:
            return JsonResponse({'error': 'User ID is required'}, status=400)

        models = Model.objects.filter(user_id=user_id)
        model_list = []
        for model in models:
            model_data = {
                'model_id': model.model_id,
                'model_name': model.model_name,
                'model_description': model.model_description,
                'status': model.status,
                'images': model.images
            }
            model_list.append(model_data)

        return JsonResponse({'models': model_list}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_random_image_by_folder(request):
    if request.method == 'GET':
        folder_url = request.GET.get('folder_url')
        if folder_url:
            folder_path = os.path.join(settings.MEDIA_ROOT, folder_url)
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
                if image_files:
                    image_name = random.choice(image_files)
                    image_path = os.path.join(folder_path, image_name)
                    with open(image_path, 'rb') as img_file:
                        return HttpResponse(img_file.read(), content_type="image/jpeg")
                else:
                    return JsonResponse({'error': 'No images found in the folder'}, status=404)
            else:
                return JsonResponse({'error': 'Folder not found or is not a directory'}, status=404)
        else:
            return JsonResponse({'error': 'Invalid parameters'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def get_model_details(request):
    if request.method == 'GET':
        model_id = request.GET.get('model_id')
        if not model_id:
            return JsonResponse({'error': 'Model ID is required'}, status=400)
        try:
            model = Model.objects.get(model_id=model_id)
            model_data = {
                'model_id': model.model_id,
                'model_name': model.model_name,
                'model_description': model.model_description,
                'status': model.status,
                'images': model.images,
            }
            return JsonResponse(model_data, status=200)
        except Model.DoesNotExist:
            return JsonResponse({'error': 'Model not found'}, status=404)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_model(request):
    if request.method == 'POST':
        try:
            model_id = request.POST.get('model_id')
            if not model_id:
                return JsonResponse({'error': 'Model ID is required'}, status=400)

            model = Model.objects.get(model_id=model_id)

            # 删除 images 和 model_path 文件夹
            if model.images:
                images_path = os.path.join(settings.MEDIA_ROOT, model.images)
                if os.path.exists(images_path):
                    shutil.rmtree(images_path)

            if model.model_path:
                model_path = os.path.join(settings.MEDIA_ROOT, model.model_path)
                if os.path.exists(model_path):
                    shutil.rmtree(model_path)

            # 删除模型记录
            model.delete()
            return JsonResponse({'message': 'Model deleted successfully'}, status=200)
        except Model.DoesNotExist:
            return JsonResponse({'error': 'Model not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
@require_GET
def get_images_by_folder(request):
    folder_url = request.GET.get('folder_url')
    if folder_url:
        folder_path = os.path.join(settings.MEDIA_ROOT, folder_url)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if image_files:
                image_data = []
                for image_name in image_files:
                    image_path = os.path.join(folder_path, image_name)
                    with open(image_path, 'rb') as img_file:
                        base64_data = base64.b64encode(img_file.read()).decode('utf-8')
                        image_data.append({
                            'name': image_name,
                            'data': base64_data
                        })
                return JsonResponse({'images': image_data}, status=200)
            else:
                return JsonResponse({'error': 'No images found in the folder'}, status=404)
        else:
            return JsonResponse({'error': 'Folder not found or is not a directory'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid parameters'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@api_view(['POST'])
def run_script(request):
    if request.data.get('flag'):
        try:
            # 使用 Popen 执行脚本
            process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                       text=True)
            # 等待进程完成
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                return Response({'message': 'Script executed', 'output': stdout})
            else:
                return Response({'error': 'Script execution failed', 'stderr': stderr}, status=500)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    else:
        return Response({'error': 'Invalid request'}, status=400)


@require_http_methods(["GET"])
def get_comments(request):
    email = request.GET.get('email')
    try:
        current_user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    comments_data = []
    comments = Comment.objects.all()
    for comment in comments:
        liked = Like.objects.filter(comment=comment, user=current_user).exists()
        comments_data.append({
            'id': comment.id,
            'content': comment.content,
            'like_count': comment.likes.count(),
            'liked': liked,
            'publish_time': comment.publish_time.strftime("%Y-%m-%d %H:%M:%S"),
            'avatar_url': comment.user.avatar_url,
            'user_name': comment.user.user_name,
        })

    return JsonResponse({'comments': comments_data}, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def toggle_like(request):
    # 明白了，问题在这，但为什么呢？直接获取不是这种格式？
    # 如果不特别指定，Axios默认将数据以Content-Type: application/json发送，后端需要相应地处理这种格式的数据。
    # Django REST framework的request.data会根据请求的Content-Type自动解析数据，无论是JSON还是表单数据，使用起来更为方便。这在构建需要处理多种数据类型的API时尤其有用。可以参见上面 run-script 用法
    try:
        data = json.loads(request.body.decode('utf-8'))
        email = data['email']
        comment_id = data['comment_id']
    except (KeyError, json.JSONDecodeError) as e:
        return JsonResponse({'error': str(e)}, status=400)

    # email = request.POST.get('email')
    # comment_id = request.POST.get('comment_id')

    try:
        user = User.objects.get(email=email)
        comment = Comment.objects.get(pk=comment_id)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'User or Comment not found'}, status=404)

    like, created = Like.objects.get_or_create(comment=comment, user=user)
    if not created:
        like.delete()  # If like already exists, delete it (toggle off)
        action = 'unliked'
    else:
        action = 'liked'

    return JsonResponse({'message': f'Comment {action}', 'like_count': comment.likes.count()})


@csrf_exempt
def create_comment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # 前端发送用户 email 和评论内容
        email = data.get('email')
        content = data.get('content')
        if email and content:
            user = User.objects.get(email=email)
            Comment.objects.create(user=user, content=content)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)





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
