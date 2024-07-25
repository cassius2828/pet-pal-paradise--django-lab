from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse


# Create your models here.


class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.color} {self.name}"

    def get_absolute_url(self):
        return reverse("toy-detail", kwargs={"pk": self.id})


class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    bio = models.TextField(max_length=250)
    tags = ArrayField(models.CharField(max_length=50), blank=True, default=list)
    img = models.CharField(
        default="https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2018/12/Vectorize-Your-Pets-Featured-Image-01.jpg"
    )
    # join table
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pet-details", kwargs={"pet_id": self.id})


class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    # fk
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} was given on {self.date}"
