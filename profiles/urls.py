from django.urls import path
from .views import profile_upsert, add_bp_reading

# Profile endpoints for authenticated users.
urlpatterns = [
    path("profile/", profile_upsert, name="profile"),
    path("reading/add/", add_bp_reading, name="add_bp_reading"),
]