"""blogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include
from .views import home_page
from accounts.views import login_page,register_page

urlpatterns = [
	re_path(r'^$',home_page,name='home'),
	re_path(r'posts/',include("posts.urls",namespace="posts")),
    re_path(r'replies/',include("replies.urls",namespace="replies")),
	re_path(r'comments/',include("comments.urls",namespace="comments")),
	re_path(r'^login/$',login_page,name='login'),
	re_path(r'^register/$',register_page,name='register'),
    path('admin/', admin.site.urls),
]
