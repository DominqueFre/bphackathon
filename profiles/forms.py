from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nhs_number", "age", "gender", "height_m", "weight_kg"]