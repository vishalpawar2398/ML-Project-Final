from django.db import models
class usermodel(models.Model):
    location = models.CharField(max_length=30)
    Bhk=models.IntegerField()
    bathroom=models.IntegerField()
    balcony=models.CharField(max_length=5)
    playground=models.CharField(max_length=5)
    landmark=models.CharField(max_length=50)
    price_range=models.IntegerField()



