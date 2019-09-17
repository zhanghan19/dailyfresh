from django.urls import path
from django.conf.urls import url
from user import views

urlpatterns = [
    path('register', views.register, name='register'),  # 注册
]
