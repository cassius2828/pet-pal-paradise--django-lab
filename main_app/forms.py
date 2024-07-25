from django import forms
from .models import Vaccine, Pet


class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ("date", "name")

        widgets = {
            "date": forms.DateInput(
                format=("%y-%m-%d"),
                attrs={"placeholder": "Select a Date", "type": "date"},
            )
        }


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ["toys"]
