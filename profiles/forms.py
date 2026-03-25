from django import forms
from .models import UserProfile, BloodPressureReading

# Only expose editable profile fields; user is attached in the view.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["nhs_number", "age", "gender", "height_m", "weight_kg"]

#Form for logging a blood pressure reading.
class BloodPressureReadingForm(forms.ModelForm):
    class Meta:
        model = BloodPressureReading
        fields = [
            "systolic",
            "diastolic",
            "pulse",
            "arm",
            "position",
            "reading_date",
            "reading_time",
            "comment",
        ]
        widgets = {
            "reading_date": forms.DateInput(attrs={"type": "date"}),
            "reading_time": forms.TimeInput(attrs={"type": "time"}),
            "comment": forms.Textarea(attrs={"rows": 3, "placeholder": "Optional notes..."}),
        }
