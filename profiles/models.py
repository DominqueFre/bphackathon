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

class BloodPressureReading(models.Model):

    # ── CHOICES ──────────────────────────────────────────────
    # These are dropdowns — the user picks from a fixed list.
    # The first value (e.g. "left") is stored in the database.
    # The second value (e.g. "Left") is what the user sees on screen.

    class ArmChoices(models.TextChoices):
        LEFT = "left", "Left"
        RIGHT = "right", "Right"

    class PositionChoices(models.TextChoices):
        SITTING = "sitting", "Sitting"
        STANDING = "standing", "Standing"
        PRONE = "prone", "Prone"

    # ── WHO DOES THIS READING BELONG TO? ─────────────────────
    # ForeignKey = "this reading belongs to ONE user"
    # A user can have many readings, but each reading has one owner.
    # on_delete=models.CASCADE means: if the user is deleted,
    #   delete all their readings too.
    # related_name="bp_readings" lets you do: user.bp_readings.all()
    #   to get all readings for a user.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bp_readings",
    )

    # ── THE ACTUAL BLOOD PRESSURE NUMBERS ────────────────────
    # Systolic = the TOP number (pressure when heart beats)
    # Diastolic = the BOTTOM number (pressure between beats)
    # Both are measured in mmHg (millimetres of mercury).

    # MinValueValidator / MaxValueValidator = stops people entering crazy numbers like -5 or 9999. Keeps the data clean.
    systolic = models.PositiveIntegerField(
        validators=[MinValueValidator(50), MaxValueValidator(300)],
        help_text="Top number (mmHg). Normal is around 120.",
    )

    diastolic = models.PositiveIntegerField(
        validators=[MinValueValidator(20), MaxValueValidator(200)],
        help_text="Bottom number (mmHg). Normal is around 80.",
    )

    # ── PULSE (HEART RATE) ───────────────────────────────────
    # Measured in beats per minute (bpm).
    # blank=True, null=True means this field is OPTIONAL.
    pulse = models.PositiveIntegerField(
        validators=[MinValueValidator(20), MaxValueValidator(250)],
        blank=True,
        null=True,
        help_text="Heart rate in beats per minute.",
    )

    # ── WHICH ARM? ───────────────────────────────────────────
    # Doctors want to know which arm was used because readings
    # can differ between arms.
    arm = models.CharField(
        max_length=5,
        choices=ArmChoices.choices,
        help_text="Which arm was the reading taken on?",
    )

    # ── BODY POSITION ────────────────────────────────────────
    # Were they sitting, standing, or lying down (prone)?
    #   Sitting  = fa-solid fa-heart-pulse
    #   Prone    = fa-solid fa-bed-pulse
    #   Standing = fa-solid fa-person
    position = models.CharField(
        max_length=8,
        choices=PositionChoices.choices,
        default=PositionChoices.SITTING,
        help_text="Body position during reading.",
    )

    # ── WHEN WAS THE READING TAKEN? ──────────────────────────
    # This is the date and time the PATIENT took the reading
    # (not when they typed it into the app). This is important for tracking trends over time.
    reading_date = models.DateField(
        help_text="Date the reading was taken.",
    )

    reading_time = models.TimeField(
        help_text="Time the reading was taken.",
    )

    # ── OPTIONAL NOTES ───────────────────────────────────────
    comment = models.TextField(
        max_length=200,
        blank=True,
        default="",
        help_text="Optional notes about this reading.",
    )

    # ── AUTOMATIC TIMESTAMPS ──────────────────────────────────────
    # created_at = automatically set when the reading is FIRST saved.
    # updated_at = automatically updated every time the reading is edited.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ordering = show newest readings first (the "-" means descending).
    class Meta:
        ordering = ["-reading_date", "-reading_time"]

    # ── WHAT SHOWS UP IN THE ADMIN PANEL ─────────────────────
    # When you see a reading in Django admin, it'll show something
    # like: "admin — 120/80 on 2026-03-25"
    def __str__(self):
        return (
            f"{self.user.username} — "
            f"{self.systolic}/{self.diastolic} on {self.reading_date}"
        )