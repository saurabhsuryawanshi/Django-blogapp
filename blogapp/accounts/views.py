from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login, get_user_model
# Create your views here.
def login_page(request):
	login_form = LoginForm(request.POST or None)
	context={
		"form":login_form
	}
	if login_form.is_valid():
		username=login_form.cleaned_data.get("username")
		password=login_form.cleaned_data.get("password")
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			# if is_safe_url(redirect_path,request.get_host()):
			# 	return redirect(redirect_path)
			# else: 
			return redirect("posts/list")
		else:
			print("Error")
	return render(request,"accounts/login.html",context)

User = get_user_model()
def register_page(request):
	form = RegisterForm(request.POST or None)
	context={
		"form":form
	}
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		email = form.cleaned_data.get("email")
		new_user=User.objects.create_user(username,email,password)
	return render(request,"accounts/register.html",context)