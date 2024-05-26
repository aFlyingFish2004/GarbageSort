from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContentViewSet, MediaViewSet, ModelViewSet

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

    path('get-by-email/<str:email>/', views.get_user_info_by_email, name='get_user_info_by_email'),
    path('userInfo/', views.userInfo, name='userInfo'),
]