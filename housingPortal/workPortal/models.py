from django.db import models
import members.models
import workers.models
import members.models

# Create your models here.
class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(members.models.CommunityAddresses, on_delete=models.CASCADE)

    title = models.TextField(max_length=1024)
    description = models.TextField(max_length=1024)
    roomOptions = [
        ('Bedroom','bedroom'),
        ('Bathroom','bathroom'),
        ('Living Room','living room'),
        ('Kitchen','kitchen'),
        ('Laundry Room','laundry room'),
        ('Garage','garage'),
        ('Yard', 'yard'),

    ]

    HousingArea = models.TextField(choices=roomOptions, null=False)
    pictures = models.ImageField()

    notes = models.TextField(max_length=1024)
    worker = models.ForeignKey(workers.models.Worker, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)