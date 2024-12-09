from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CommunityAddresses(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.address}'

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    firstName = models.TextField(max_length=1024)
    lastName = models.TextField(max_length=1024)
    address = models.ForeignKey(CommunityAddresses, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'