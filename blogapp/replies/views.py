from django.shortcuts import render
from .models import Reply
from django.contrib.auth import get_user_model
from comments.models import Comment
from django.utils import timezone
# Create your views here.
User=get_user_model()
def reply_create_view(request):
	if request.is_ajax():
		user_id=request.POST.get('user_id')
		user=User.objects.filter(username=user_id).last()
		comment_id=request.POST.get('comment_id')
		comment=Comment.objects.filter(id=comment_id).last()
		now=timezone.now()
		content=request.POST.get('reply_content')
		reply=Reply.objects.create(user_id=user,comment_id=comment,content=content,created_on=now)
	return render(request,"list.html",{})
