from django.shortcuts import render , redirect
from django.conf import settings

User=settings.AUTH_USER_MODEL

def home_page(request):
	return render(request,"index.html",{})

