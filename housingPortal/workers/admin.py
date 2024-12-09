from django.contrib import admin
# Register your models here.
from .models import *


# Register your models here.
integratedModels = [
    Company,
    Worker
]
for i in integratedModels:
    admin.site.register(i)