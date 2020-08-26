from django.shortcuts import render , redirect
from django.contrib.auth import authenticate,login, get_user_model
from django import forms
from django.contrib.auth import get_user_model
from django.utils.http import is_safe_url

User = get_user_model()

class LoginForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(label='confirm password', widget=forms.PasswordInput)
	email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"your email"}))

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError("username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("email already exists")
		return email

	def clean(self):
		data=self.cleaned_data
		password=self.cleaned_data.get("password")
		password2=self.cleaned_data.get("password2")
		if password != password2:
			raise forms.ValidationError("Enter the matching Password")
		return data 