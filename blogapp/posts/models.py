from django.db import models
from django.urls import reverse
from django.conf import settings

User=settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
	user_id=models.ManyToManyField(User,null=True,blank=True)
	title=models.CharField(max_length=120,null=True,blank=True)
	content=models.TextField(null=True,blank=True)
	created_on=models.DateTimeField(null=True,blank=True)
	updated_on=models.DateTimeField(null=True,blank=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:detail",kwargs={"id":self.id})

	class Meta:
		ordering=['-created_on']