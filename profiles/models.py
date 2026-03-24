from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

class UserProfile(models.Model):
    class GenderChoices(models.TextChoices):
        FEMALE = "female", "Female"
        MALE = "male", "Male"
        NON_BINARY = "non_binary", "Non-binary"
        PREFER_NOT_TO_SAY = "prefer_not_to_say", "Prefer not to say"

    # One profile record per authenticated user.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    
    # ERD baseinfo.nhs_number is varchar(12)
    nhs_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{3}\s?\d{3}\s?\d{4}$",
                message="Enter NHS number as 10 digits, e.g. 123 456 7890.",
            )
        ],
        help_text="10 digits. Spaces allowed.",
    )

    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(120)]
    )
    
    gender = models.CharField(
        max_length=20,
        choices=GenderChoices.choices,
        default=GenderChoices.PREFER_NOT_TO_SAY,
    )

    # ERD height is metres (m), store to 2 decimal places
    height_m = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.50")), MaxValueValidator(Decimal("2.50"))],
        help_text="Height in metres, e.g. 1.75",
    )
    
    # ERD weight is kilograms (Kg)
    weight_kg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("10.00")), MaxValueValidator(Decimal("500.00"))],
        help_text="Weight in kilograms, e.g. 72.40",
    )

    # Audit timestamps for basic record tracking.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def bmi(self):
        # BMI = kg / m^2
        if not self.height_m or self.height_m <= 0:
            return None
        # Round to one decimal place for display consistency.
        value = Decimal(self.weight_kg) / (Decimal(self.height_m) * Decimal(self.height_m))
        return value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)

    def __str__(self):
        return f"{self.user.username} profile"