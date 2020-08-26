from django.urls import path,re_path
from .views import (
	reply_create_view
)
app_name="replies"
urlpatterns=[
	re_path(r'^create/$',reply_create_view,name='create'),
]