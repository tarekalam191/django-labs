from django.db import models

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    publishDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    version = models.IntegerField(default=1)
    latestVersion = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
