from django.test import TestCase
from profiles.forms import UserProfileForm, BloodPressureReadingForm
from decimal import Decimal

class UserProfileFormTests(TestCase):

    def test_valid_profile_form(self):
        form = UserProfileForm(data={
            "nhs_number": "123 456 7890",
            "age": 25,
            "gender": "male",
            "height_m": Decimal("1.75"),
            "weight_kg": Decimal("70.00"),
        })
        self.assertTrue(form.is_valid())

    def test_invalid_nhs_number(self):
        form = UserProfileForm(data={
            "nhs_number": "abc123",
            "age": 25,
            "gender": "male",
            "height_m": Decimal("1.75"),
            "weight_kg": Decimal("70.00"),
        })
        self.assertFalse(form.is_valid())


class BloodPressureReadingFormTests(TestCase):

    def test_valid_reading_form(self):
        form = BloodPressureReadingForm(data={
            "systolic": 120,
            "diastolic": 80,
            "pulse": 70,
            "arm": "left",
            "position": "sitting",
            "reading_date": "2024-01-01",
            "reading_time": "12:00",
        })
        self.assertTrue(form.is_valid())

    def test_invalid_systolic(self):
        form = BloodPressureReadingForm(data={
            "systolic": 5,  # too low
            "diastolic": 80,
            "pulse": 70,
            "arm": "left",
            "position": "sitting",
            "reading_date": "2024-01-01",
            "reading_time": "12:00",
        })
        self.assertFalse(form.is_valid())
