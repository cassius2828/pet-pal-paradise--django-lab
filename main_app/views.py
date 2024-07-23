from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from .models import Pet, Toy
from .forms import VaccineForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def pets_index(request):
    pets = Pet.objects.all()
    return render(request, "pets/index.html", {"pets": pets})


def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    vaccine_form = VaccineForm()
    return render(
        request, "pets/details.html", {"pet": pet, "vaccine_form": vaccine_form}
    )


class PetCreate(CreateView):
    model = Pet
    fields = "__all__"


class PetUpdate(UpdateView):
    model = Pet
    fields = [
        "price",
        "age",
        "bio",
        "tags",
    ]


class PetDelete(DeleteView):
    model = Pet
    success_url = "/pets/"


def add_vaccine(request, pet_id):
    form = VaccineForm(request.POST)
    if form.is_valid():

        new_vaccine = form.save(commit=False)

        new_vaccine.pet_id = pet_id
        new_vaccine.save()
    return redirect("pet_details", pet_id=pet_id)


class ToyCreate(CreateView):
    model = Toy
    fields = "__all__"


class ToyDetail(DetailView):
    model = Toy


class ToyList(ListView):
    model = Toy


class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]


class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"
