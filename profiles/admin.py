from django.contrib import admin
from .models import UserProfile
from .models import BloodPressureReading

# Register profile with useful columns so BMI and core metrics are visible in admin list view.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nhs_number", "age", "gender", "height_m", "weight_kg", "bmi")
    search_fields = ("user__username", "nhs_number")
    list_filter = ("gender",)

@admin.register(BloodPressureReading)
class BloodPressureReadingAdmin(admin.ModelAdmin):
    list_display = ("user", "systolic", "diastolic", "pulse", "arm", "position", "reading_date")
    list_filter = ("arm", "position")
    search_fields = ("user__username",)
