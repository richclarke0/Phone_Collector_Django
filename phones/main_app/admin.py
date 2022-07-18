from django.contrib import admin
# Register your models here.
from .models import Phone, Accessory
admin.site.register(Phone)
admin.site.register(Accessory)