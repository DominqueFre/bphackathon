from django.urls import path
from .views import profile_upsert

# Profile endpoints for authenticated users.
urlpatterns = [
    path("profile/", profile_upsert, name="profile"),
]