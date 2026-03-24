from django import forms
from .models import UserProfile


# Only expose editable profile fields; user is attached in the view.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nhs_number", "age", "gender", "height_m", "weight_kg"]