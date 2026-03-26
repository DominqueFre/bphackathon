from django.urls import path
from .views import profile_upsert, add_bp_reading, bp_reading_list

urlpatterns = [
    path("profile/", profile_upsert, name="profile"),
    path("reading/add/", add_bp_reading, name="add_bp_reading"),
    path("readings/", bp_reading_list, name="bp_reading_list"),
]