from django.db import models

# Create your models here.
class Home(models.Model):
    name=models.CharField(max_length=20,blank=False)
    username=models.CharField(max_length=20,blank=False)
    email=models.EmailField()
    dob=models.DateField()
    age=models.IntegerField()
    password=models.CharField(max_length=20,blank=False)

    
