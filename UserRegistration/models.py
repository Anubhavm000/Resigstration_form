from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length = 50)
    classname = models.CharField(max_length = 50)
    institution = models.EmailField(max_length = 256)
    phone1 = models.CharField(max_length = 10)
    email = models.CharField(max_length =  256)
    interest = models.CharField(max_length =  256)
    workedearlier = models.CharField(max_length =  256)
    attended = models.CharField(max_length =  256)
    training = models.CharField(max_length =  256)
    join = models.CharField(max_length =  256)
  