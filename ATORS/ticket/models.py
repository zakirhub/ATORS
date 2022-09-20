from distutils.archive_util import make_zipfile
import email
from email.mime import image
from operator import mod
from turtle import title
from django.db import models

# Create your models here.
class Booked_Ticket(models.Model):
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=15, null=True)
    flying_from = models.CharField(max_length=50)
    flying_to = models.CharField(max_length=50)
    departing_date = models.DateField()
    return_date = models.DateField()
    adults = models.CharField(max_length=5)
    childrens = models.CharField(max_length=5)
    travel_class = models.CharField(max_length=10)
    