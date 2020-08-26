from django.db import models
from django.conf import settings
User=settings.AUTH_USER_MODEL
from comments.models import Comment
# Create your models here.
class Reply(models.Model):
	user_id=models.ForeignKey(User,models.SET_NULL,null=True)
	comment_id=models.ForeignKey(Comment,models.SET_NULL,null=True)
	content=models.TextField()
	created_on=models.DateTimeField()
	updated_on=models.DateTimeField(null=True)


	def __str__(self):
		return self.content

	class Meta:
		ordering=['-created_on']
