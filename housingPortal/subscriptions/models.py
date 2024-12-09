from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
# Create your models here.

class SubscriptionPlan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in days")  # e.g., 30 for monthly
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Subscription Plan"  # Singular form
        verbose_name_plural = "Subscription Plans"  # Plural form
    

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=now)
    end_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.plan.duration)
        super().save(*args, **kwargs)

    def is_active(self):
        return self.end_date > now()
    
