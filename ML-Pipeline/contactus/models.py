from django.db import models

class contacmodel(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Message=models.CharField(max_length=200)

