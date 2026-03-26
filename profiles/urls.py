from django.urls import path
from .views import (
    profile_detail,
    profile_upsert,
    add_bp_reading,
    bp_reading_list,
    edit_bp_reading,
    delete_bp_reading,
)

urlpatterns = [
    path("profile/", profile_detail, name="profile"),
    path("profile/edit/", profile_upsert, name="profile_edit"),

    path("reading/add/", add_bp_reading, name="add_bp_reading"),
    path("readings/", bp_reading_list, name="bp_reading_list"),
    path("reading/<int:pk>/edit/", edit_bp_reading, name="edit_bp_reading"),
    path("reading/<int:pk>/delete/", delete_bp_reading, name="delete_bp_reading"),
]
