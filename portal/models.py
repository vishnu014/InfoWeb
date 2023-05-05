from django.db import models

# Create your models here.


class Blog(models.Model):
    title= models.CharField(max_length=100)
    thumbnail=models.ImageField(upload_to='media/thumbnail')

class BlogContents(models.Model):
    content=models.CharField(max_length=200)
    content_image=models.ImageField(upload_to="media/content_image")