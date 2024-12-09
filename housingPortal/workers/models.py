from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    id = models.BigIntegerField(primary_key=True)
    companyName = models.TextField(max_length = 1024)
    companyAddress = models.TextField(max_length = 1024)
    companyContact = models.BigIntegerField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Worker(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    firstName = models.TextField(max_length = 1024)
    lastName = models.TextField(max_length = 1024)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    contactNumber = models.BigIntegerField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)