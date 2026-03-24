from django.urls import path
from .views import profile_upsert

urlpatterns = [
    path("profile/", profile_upsert, name="profile"),
]