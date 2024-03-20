from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class post(models.Model): # Changed to CamelCase
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField('Tag') # Use string-based reference

class Tag(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField('post') # Use string-based reference

class BlockedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blocked_user = models.ForeignKey(User, related_name='blocked_by', on_delete=models.CASCADE)
