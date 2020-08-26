from django.urls import path,re_path
from .views import (
	post_list_view,
	post_detail_view,
	post_create_view
)

app_name="posts"

urlpatterns=[
	re_path(r'^list/$',post_list_view,name='list'),
	re_path(r'^create/$',post_create_view,name='create'),
	re_path(r'^(?P<id>[\w-]+)/$',post_detail_view,name='detail'),
]