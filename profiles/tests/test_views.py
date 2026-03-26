from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import UserProfile, BloodPressureReading
from decimal import Decimal

class ViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.client.login(username="testuser", password="pass1234")

    def test_profile_page_loads(self):
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile_detail.html")

    def test_profile_edit_page_loads(self):
        response = self.client.get(reverse("profile_edit"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profiles_form.html")

    def test_add_reading(self):
        response = self.client.post(reverse("add_bp_reading"), {
            "systolic": 120,
            "diastolic": 80,
            "pulse": 70,
            "arm": "left",
            "position": "sitting",
            "reading_date": "2024-01-01",
            "reading_time": "12:00",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BloodPressureReading.objects.count(), 1)

    def test_reading_list_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("bp_reading_list"))
        self.assertEqual(response.status_code, 302)  # redirect to login
