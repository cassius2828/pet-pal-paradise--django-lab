from django.contrib import admin

# Register your models here.
from .models import Pet, Vaccine,Toy

admin.site.register(Pet)
admin.site.register(Vaccine)
admin.site.register(Toy)