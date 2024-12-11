from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField  # Import the PhoneNumberField

# Create your models here.
class Community(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=1024)
    logo = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=1024)
    district_map = models.ImageField(upload_to='images/', null=True)
    class Meta:
        verbose_name = "Community"  # Singular form
        verbose_name_plural = "Community"  # Plural form

    def __str__(self):
        return f'{self.name}'
    

class CommunityAddresses(models.Model):
    id = models.AutoField(primary_key=True)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True)
    address = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Community Address"  # Singular form
        verbose_name_plural = "Community Addresses"  # Plural form
    
    def __str__(self):
        return f'{self.address}'

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    firstName = models.TextField(max_length=60)
    lastName = models.TextField(max_length=60)
    address = models.ForeignKey(CommunityAddresses, on_delete= models.CASCADE)
    email = models.EmailField(null=True)
    phone = models.BigIntegerField(null=True, blank = True)
    photo = models.ImageField(upload_to='images/' ,null=True)
    # phone = PhoneNumberField(null=True, blank=True)  # Using PhoneNumberField here

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
    