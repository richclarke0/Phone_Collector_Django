from django.contrib import admin
# Register your models here.
from .models import Phone, Accessory, Band, Photo
admin.site.register(Phone)
admin.site.register(Accessory)
admin.site.register(Band)
admin.site.register(Photo)