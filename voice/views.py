from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess

import os
from django.conf import settings

from django.http import JsonResponse

from django.db.models import Prefetch

# 获取项目根目录
base_dir = settings.BASE_DIR

# 构建脚本的绝对路径
# script_path = os.path.join(base_dir, 'voice', 'voice2.py')
script_path = os.path.join(base_dir, 'voice', 'voice3.py')



# @api_view(['POST'])
# def run_script(request):
#     if request.data.get('flag'):
#         try:
#             # 调用你的Python脚本
#             result = subprocess.run(['python', script_path], capture_output=True, text=True, encoding='utf-8')
#             # print(Response({'message': 'Script executed', 'output': result.stdout}))
#             return JsonResponse({'message': 'Script executed', 'output': result.stdout})
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)


@api_view(['POST'])
def run_script(request):

    if request.data.get('flag'):
        try:
            # 使用 Popen 执行脚本
            process = subprocess.Popen(['python', script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
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


# # 获取所有评论
# def get_comments(request):
#     # 使用select_related进行关联查询以优化性能
#     comments = Comment.objects.select_related('user').all()
#
#     # 将查询集转换为包含所需数据的列表
#     comments_list = [
#         {
#             'id': comment.id,  # 添加主键id
#             'content': comment.content,
#             'user_name': comment.user.user_name,
#             'publish_time': comment.publish_time.isoformat(),  # 格式化发布时间为ISO格式
#             'like': comment.like,
#             'avatar_url': comment.user.avatar_url,
#             'email': comment.user.email,
#         } for comment in comments
#     ]
#
#     # 返回JSON响应
#     return JsonResponse(comments_list, safe=False)

# if __name__ == '__main__':
#     get_comments()
