from django import forms
from WorldOfSpeedApp.car.models import Car

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("type", "model", "year", "image_url", "price")

        widgets = {
            "type": forms.Select(
                 attrs={
                    "placeholder": "Type"
                }
            ),
            "model": forms.TextInput(
                 attrs={
                    "placeholder": "Model"
                }
            ),
            "year": forms.IntegerField(),
            "image_url": forms.TextInput(
                attrs={
                    "placeholder": "https://..."
                }
            ),
            "price": forms.IntegerField()
        }
