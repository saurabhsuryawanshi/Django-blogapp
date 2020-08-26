from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
from posts.models import Post
# Create your models here.
class Comment(models.Model):
	user_id=models.ManyToManyField(User,null=True)
	post_id=models.ForeignKey(Post,models.SET_NULL,null=True)
	content=models.TextField()
	created_on=models.DateTimeField(null=True,blank=True)
	updated_on=models.DateTimeField(null=True,blank=True)


	def __str__(self):
		return self.content

	class Meta:
		ordering=['-created_on']