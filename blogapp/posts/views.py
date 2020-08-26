from django.shortcuts import render
from posts.models import Post
from comments.models import Comment
from replies.models import Reply
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your views here.
User=get_user_model()
# Create your views here.
def post_list_view(request):
	post=Post.objects.all()
	context={
		"post":post
	}
	return render(request,"list.html",context)

def post_detail_view(request,*args,**kwargs):
	id=kwargs['id']
	post=Post.objects.filter(id=id).last()
	comments=Comment.objects.filter(post_id=id)
	context={
		"post":post,
		"comments":comments
	}
	return render(request,"post_detail.html",context)

def post_create_view(request):
	if request.method=="POST":
		user_id=request.POST.get('user_id')
		title=request.POST.get('title')
		content=request.POST.get('post_content')
	now=timezone.now()
	post=Post(title=title,content=content,created_on=now)
	post.save()
	user=User.objects.filter(username=user_id).last()
	post.user_id.add(user)
	post=Post.objects.all()
	context={
		"post":post
	}
	return render(request,"list.html",context)