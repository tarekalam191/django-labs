from django.db import models

class Book(models.Model):  
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    publish_date=models.DateTimeField(auto_now_add=True)
    version=models.IntegerField(default=1)
    latest_version=models.DateTimeField(auto_now=True)
    image=models.CharField(max_length=200,null=True)
