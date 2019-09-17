from django.urls import path
from django.conf.urls import include, url
from goods import views

urlpatterns = [
    path('', views.index, name='index')
]