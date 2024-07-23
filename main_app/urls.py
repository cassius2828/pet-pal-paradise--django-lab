from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.pets_index, name="pets_index"),
    path("pets/<int:pet_id>", views.pet_details, name="pet_details"),
    path("pets/create/", views.PetCreate.as_view(), name="pet_create"),
    path("pets/<int:pk>/update/", views.PetUpdate.as_view(), name="pet_update"),
    path("pets/<int:pk>/delete", views.PetDelete.as_view(), name="pet_delete"),
    path("pets/<int:pet_id>/add_vaccine", views.add_vaccine, name="add_vaccine")
]
