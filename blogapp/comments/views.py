from django.shortcuts import render,redirect
from comments.models import Comment
from posts.models import Post
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your views here.
User=get_user_model()
def comment_create_view(request):
	if request.method=="POST":
		comment_content=request.POST.get('comment_text')
		user_id=request.POST.get('user_id')
		post_id=request.POST.get('post_id')
		post=Post.objects.filter(id=post_id).last()
		now=timezone.now()
		comment=Comment(post_id=post,content=comment_content,created_on=now)
		comment.save()
		user=User.objects.filter(username=user_id).last()
		comment.user_id.add(user)
		return redirect("posts/list")
	return render(request,"list.html",{})