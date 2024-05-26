from django.urls import path
from . import views

urlpatterns = [
    path('run-script/', views.run_script, name='run-script'),
]

