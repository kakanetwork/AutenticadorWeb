from django.db import models

# Create your models here.
class Usuario_BD(models.Model): 
    id_user = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)    
