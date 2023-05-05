from django.db import models

# Create your models here.

class Register(models.Model):
    email=models.EmailField(max_length=100)
    password=models.TextField(max_length=100)
    username=models.CharField(max_length=100)
    
