from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView, ListView
from .models import Pet, Toy
from .forms import VaccineForm, PetForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ///////////////////////////
# Function Views
# ///////////////////////////

# Home page view
def home(request):
    return render(request, "home.html")

# View to list all pets, requires login
@login_required
def pets_index(request):
    pets = Pet.objects.all()
    return render(request, "pets/index.html", {"pets": pets})

# View to show details of a specific pet, requires login
@login_required
def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    toys = Toy.objects.exclude(id__in=pet.toys.all().values_list("id"))
    vaccine_form = VaccineForm()
    return render(
        request,
        "pets/details.html",
        {"pet": pet, "vaccine_form": vaccine_form, "toys": toys},
    )

# View to add a vaccine to a pet
def add_vaccine(request, pet_id):
    form = VaccineForm(request.POST)
    if form.is_valid():
        new_vaccine = form.save(commit=False)
        new_vaccine.pet_id = pet_id
        new_vaccine.save()
    return redirect("pet_details", pet_id=pet_id)

# View to associate a toy with a pet
def associate_toy(request, pet_id, toy_id):
    pet = Pet.objects.get(id=pet_id)
    pet.toys.add(toy_id)
    return redirect("pet_details", pet_id=pet_id)

# View to remove a toy from a pet
def remove_toy(request, pet_id, toy_id):
    pet = Pet.objects.get(id=pet_id)
    pet.toys.remove(toy_id)
    return redirect("pet_details", pet_id=pet_id)

# User signup view
def signup(request):
    error_message = ""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("pet_index")
        else:
            error_message = "Invalid Signup. Try Again."
    form = UserCreationForm()
    return render(
        request, "signup.html", {"error_message": error_message, "form": form}
    )

# ///////////////////////////
# Class Based Views
# ///////////////////////////

# Create view for Pet model, requires login
class PetCreate(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm

# Update view for Pet model, requires login
class PetUpdate(LoginRequiredMixin, UpdateView):
    model = Pet
    fields = ["price", "age", "bio", "tags"]

# Delete view for Pet model
class PetDelete(DeleteView):
    model = Pet
    success_url = "/pets/"

# Create view for Toy model, requires login
class ToyCreate(LoginRequiredMixin, CreateView):
    model = Toy
    fields = "__all__"

# Detail view for Toy model, requires login
class ToyDetail(LoginRequiredMixin, DetailView):
    model = Toy

# List view for Toy model, requires login
class ToyList(LoginRequiredMixin, ListView):
    model = Toy

# Update view for Toy model
class ToyUpdate(UpdateView):
    model = Toy
    fields = ["name", "color"]

# Delete view for Toy model
class ToyDelete(DeleteView):
    model = Toy
    success_url = "/toys/"
