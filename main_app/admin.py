from django.contrib import admin

# Register your models here.
from .models import Pet, Vaccine

admin.site.register(Pet)
admin.site.register(Vaccine)
