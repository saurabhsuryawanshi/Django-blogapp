from django.urls import path,re_path,include
from comments.views import(
	comment_create_view
)
app_name="comments"
urlpatterns=[
	re_path(r'^create/$',comment_create_view,name="create")
]
