"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path, include
from QuesAns.views import CommentsAPI, AddCommentAPI, DeleteCommentAPI, EditCommentAPI
from rest_framework import routers, serializers, viewsets
from QuesAns.models import Comment
from rest_framework.response import Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CommentsAPI.as_view()),
    path('get_all_comments/', CommentsAPI.as_view()),
    path('create_comment/', AddCommentAPI.as_view()),
    path('delete_comment/', DeleteCommentAPI.as_view()),
    path('edit_comment/', EditCommentAPI.as_view())
]
