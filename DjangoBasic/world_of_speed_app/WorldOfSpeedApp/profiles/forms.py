from django import forms
from WorldOfSpeedApp.profiles.models import Profile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("username", "email", "age", "password")
        
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "Username"
                }
            ),
               
            "email": forms.EmailInput(
                 attrs={
                    "placeholder": "Email"
                }
            ),
            "age": forms.NumberInput(
                 attrs={
                    "placeholder": "Age"
                }
            ),
            "password": forms.PasswordInput(
                 attrs={
                    "placeholder": "Password"
                }
            ),
        }
        
        help_texts = {
            "age": "Age requirement: 21 years and above."
        }
        
  