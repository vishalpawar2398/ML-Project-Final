from django.db import models

class Userinputmodel(models.Model):
    area_type=models.CharField(max_length=100)
    availability=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    bhk=models.IntegerField()
    society=models.CharField(max_length=100)
    total_sqft=models.IntegerField()
    bath = models.IntegerField()
    balcony = models.CharField(max_length=100)
    price=models.IntegerField()

