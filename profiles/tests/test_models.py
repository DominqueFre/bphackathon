from django.test import TestCase
from django.contrib.auth.models import User
from decimal import Decimal
from profiles.models import UserProfile, BloodPressureReading

class UserProfileModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            nhs_number="123 456 7890",
            age=30,
            gender="male",
            height_m=Decimal("1.80"),
            weight_kg=Decimal("81.00"),
        )

    def test_bmi_calculation(self):
        self.assertEqual(self.profile.bmi, Decimal("25.0"))

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "testuser profile")


class BloodPressureReadingModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="reader", password="pass1234")
        self.reading = BloodPressureReading.objects.create(
            user=self.user,
            systolic=120,
            diastolic=80,
            pulse=70,
            arm="left",
            position="sitting",
            reading_date="2024-01-01",
            reading_time="12:00",
        )

    def test_reading_str(self):
        self.assertIn("reader — 120/80", str(self.reading))
