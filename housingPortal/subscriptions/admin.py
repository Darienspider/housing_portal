from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


# Register your models here.
integratedModels = [
    Subscription,
    SubscriptionPlan
]
for i in integratedModels:
    admin.site.register(i)