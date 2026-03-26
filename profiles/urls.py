from django.urls import path
from .views import profile_upsert, add_bp_reading, bp_reading_list, edit_bp_reading, delete_bp_reading

urlpatterns = [
    path("profile/", profile_upsert, name="profile"),
    path("reading/add/", add_bp_reading, name="add_bp_reading"),
    path("readings/", bp_reading_list, name="bp_reading_list"),
    path("reading/<int:pk>/edit/", edit_bp_reading, name="edit_bp_reading"),
    path("reading/<int:pk>/delete/", delete_bp_reading, name="delete_bp_reading"),
]