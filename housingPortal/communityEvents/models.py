from django.db import models
from django.contrib.auth.models import User
from members.models import CommunityAddresses
# Create your models here.
class CommunityEvents(models.Model):
    id = models.AutoField(primary_key=True)
    event_time = models.DateTimeField(null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    event_title = models.TextField(max_length=25, null=True)
    description = models.TextField(max_length=1024)
    address = models.TextField(max_length=1024)
    
    class Meta:
        verbose_name_plural = "Community Events"  # Plural form

    def __str__(self):
        return f' {self.organizer} - {self.event_title}'