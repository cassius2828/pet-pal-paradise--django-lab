from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pets/', views.pets_index, name="pets_index"),
    path('pets/<int:pet_id>', views.pet_details, name="pet_details")
]