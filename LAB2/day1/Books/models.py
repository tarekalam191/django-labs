from django.db import models
from author.models import *

class Book(models.Model):  
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(auto_now_add=True)
    version = models.IntegerField(default=1) 
    latest_version = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='Books/images',null=True)
    author = models.ForeignKey('author.Author', on_delete=models.CASCADE, default=1)
