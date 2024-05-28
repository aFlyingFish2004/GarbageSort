from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContentViewSet, MediaViewSet, ModelViewSet
from django.views.static import serve

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'media', MediaViewSet)
router.register(r'models', ModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('index/', views.index, name='index'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('account/', views.account_view, name='account'),

    path('upload/', views.upload_image, name='upload_image'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
    path('get_image/', views.get_image, name='get_image'),
    path('get_message/', views.get_message, name='get_message'),
    path('infer/', views.infer_view, name='infer'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),

    path('create_model/', views.create_model, name='create_model'),
    path('update_model/', views.update_model, name='update_model'),
    path('upload_images/', views.upload_images, name='upload_images'),
    path('get_image_by_path/', views.get_image_by_path, name='get_image_by_path'),
    path('get_models/', views.get_models, name='get_models'),
    path('get_random_image_by_folder/', views.get_random_image_by_folder, name='get_random_image_by_folder'),
    path('get_model_details/', views.get_model_details, name='get_model_details'),
    path('delete_model/', views.delete_model, name='delete_model'),
    path('get_images_by_folder/', views.get_images_by_folder, name='get_images_by_folder'),

    path('run-script/', views.run_script, name='run-script'),
    path('userInfo/', views.userInfo, name='userInfo'),
    path('get-by-email/<str:email>/', views.get_user_info_by_email, name='get_user_info_by_email'),
    path('comments/', views.get_comments, name='get_comments'),
    path('toggle_like/', views.toggle_like, name='toggle_like'),
    path('comments/create/', views.create_comment, name='create_comment'),
]
