from django.db import models
from django.conf import settings

class Comment(models.Model):
	user = models.CharField(default="Anonymous", max_length=100)
	comment_body = models.TextField()
	is_sub_comment = models.BooleanField()
	parent_id = models.IntegerField()
	






