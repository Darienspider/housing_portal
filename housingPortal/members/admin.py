from django.contrib import admin
from .models import *


# Register your models here.
integratedModels = [
    CommunityAddresses,
    Member,
    Community,
]
for i in integratedModels:
    admin.site.register(i)