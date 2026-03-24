from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "nhs_number", "age", "gender", "height_m", "weight_kg", "bmi")
    search_fields = ("user__username", "nhs_number")
    list_filter = ("gender",)
