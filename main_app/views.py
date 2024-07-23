from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Pet
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


# class Pet:
#     def __init__(self, name, species, age, price, bio, tags, img):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.price = price
#         self.bio = bio
#         self.tags = tags
#         self.img = img

# # Creating 10 pet instances
# pet1 = Pet(
#     name="Buddy",
#     species="Dog",
#     age=3,
#     price=200,
#     bio="Buddy is a friendly golden retriever who loves to play fetch.",
#     tags=["friendly", "energetic", "loyal"],
#     img="https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSWhkuVCo1_0UpZ7-BfDTbTNB9Nx-3FoQprHTX48rdN2AYryK_zS2YZ6qxmlJFarvcZjZqXnKhrBe2aTKnSQm2jH2gSVI8b1V75dhbrjg"
# )

# pet2 = Pet(
#     name="Whiskers",
#     species="Cat",
#     age=2,
#     price=150,
#     bio="Whiskers is a curious tabby cat who enjoys lounging in the sun.",
#     tags=["curious", "independent", "playful"],
#     img="https://i.natgeofe.com/n/548467d8-c5f1-4551-9f58-6817a8d2c45e/NationalGeographic_2572187_square.jpg"
# )

# pet3 = Pet(
#     name="Charlie",
#     species="Parrot",
#     age=4,
#     price=300,
#     bio="Charlie is a colorful parrot that loves to mimic sounds and talk.",
#     tags=["talkative", "colorful", "intelligent"],
#     img="https://i.ebayimg.com/images/g/s6cAAOSwl2BeTtN9/s-l1200.webp"
# )

# pet4 = Pet(
#     name="Nibbles",
#     species="Rabbit",
#     age=1,
#     price=50,
#     bio="Nibbles is a cute bunny that loves to chew on carrots and hop around.",
#     tags=["cute", "gentle", "quiet"],
#     img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuTNMS8yzQ3Y6_kn3lGPgZmp_pMRTp3I-TONBWv-3qXEG7Dt6CpH3-GNYzw43Q_didD03VpfHUmVZ7BtOexqURA-TU5BV6CiDi3lCeMA"
# )

# pet5 = Pet(
#     name="Goldie",
#     species="Fish",
#     age=0,
#     price=20,
#     bio="Goldie is a bright goldfish that adds a touch of serenity to any home.",
#     tags=["peaceful", "easy-care", "colorful"],
#     img="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Common_goldfish.JPG/800px-Common_goldfish.JPG"
# )

# pet6 = Pet(
#     name="Rex",
#     species="Dog",
#     age=5,
#     price=250,
#     bio="Rex is a strong and protective German Shepherd, perfect for a family guard dog.",
#     tags=["protective", "strong", "loyal"],
#     img="https://www.dogster.com/wp-content/uploads/2021/12/german-shepherd-dog-standing-at-the-park_Bildagentur-Zoonar-GmbH_Shutterstock.jpeg"
# )

# pet7 = Pet(
#     name="Shadow",
#     species="Cat",
#     age=3,
#     price=120,
#     bio="Shadow is a sleek black cat with a mysterious and loving personality.",
#     tags=["loving", "mysterious", "independent"],
#     img="https://image.petmd.com/files/inline-images/black-cat-breeds-manx.jpg?VersionId=r4qTZpY8EBNUMGt4GUI7CI1PVpmr6qul"
# )

# pet8 = Pet(
#     name="Tweety",
#     species="Bird",
#     age=2,
#     price=75,
#     bio="Tweety is a small canary that loves to sing melodious tunes.",
#     tags=["musical", "small", "cheerful"],
#     img="https://www.omlet.us/images/originals/canary-perched-in-outside-aviary.jpg"
# )

# pet9 = Pet(
#     name="Spike",
#     species="Hedgehog",
#     age=2,
#     price=100,
#     bio="Spike is a quirky hedgehog with a shy but playful nature.",
#     tags=["quirky", "shy", "playful"],
#     img="https://vetmed.illinois.edu/wp-content/uploads/2021/04/pc-keller-hedgehog.jpg"
# )

# pet10 = Pet(
#     name="Sasha",
#     species="Dog",
#     age=0,
#     price=220,
#     bio="Sasha is a Siberian Husky with beautiful blue eyes and a friendly demeanor.",
#     tags=["beautiful", "friendly", "energetic"],
#     img="https://bamahuskies.com/wp-content/uploads/2023/04/about-husky-image.jpg"
# )

# List of all pet instances
# pets = [pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9, pet10]
# default image https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2018/12/Vectorize-Your-Pets-Featured-Image-01.jpg
