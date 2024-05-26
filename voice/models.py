from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=50, unique=True, db_index=True)
#     password_hash = models.CharField(max_length=255)
#     email = models.EmailField(max_length=100, unique=True, db_index=True)
#     avatar_url = models.URLField(max_length=255, blank=True, null=True)
#     registration_time = models.DateTimeField(default=timezone.now)
#     update_time = models.DateTimeField(auto_now=True)
#     score = models.IntegerField(default=0)
#
#
#     def __str__(self):
#         return self.user_name


# class Comment(models.Model):
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # 使用ForeignKey关联User模型
#     like = models.IntegerField(default=0)  # 假设like是一个整数，表示点赞数
#     publish_time = models.DateTimeField(default=timezone.now)  # 添加发布时间字段
#
#     def __str__(self):
#         return self.content[:50]  # 返回content的前50个字符作为字符串表示














