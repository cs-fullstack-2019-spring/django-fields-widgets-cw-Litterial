from django.db import models

# Create your models here.
class HeroApplication(models.Model):
    name=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    powers=models.CharField(max_length=200)
    power_type=models.CharField(max_length=200)
    alignment=models.CharField(max_length=200)
    example=models.CharField(max_length=200)