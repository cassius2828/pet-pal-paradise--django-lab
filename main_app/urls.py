from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.pets_index, name="pets-index"),
    path("pets/<int:pet_id>", views.pet_details, name="pet-details"),
    path("pets/create/", views.PetCreate.as_view(), name="pet-create"),
    path("pets/<int:pk>/update/", views.PetUpdate.as_view(), name="pet-update"),
    path("pets/<int:pk>/delete", views.PetDelete.as_view(), name="pet-delete"),
    path("pets/<int:pet_id>/add_vaccine", views.add_vaccine, name="add-vaccine"),
    path("toys/create/", views.ToyCreate.as_view(), name="toy-create"),
    path("toys/<int:pk>/", views.ToyDetail.as_view(), name="toy-detail"),
    path("toys/", views.ToyList.as_view(), name="toy-index"),
    path("toys/<int:pk>/update/", views.ToyUpdate.as_view(), name="toy-update"),
    path("toys/<int:pk>/delete/", views.ToyDelete.as_view(), name="toy-delete"),
    path(
        "pets/<int:pet_id>/associate-toy/<int:toy_id>/",
        views.associate_toy,
        name="associate-toy",
    ),
    path(
        "pets/<int:pet_id>/remove-toy/<int:toy_id>/",
        views.remove_toy,
        name="remove-toy",
    ),
]
