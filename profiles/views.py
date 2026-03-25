from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import UserProfileForm, BloodPressureReadingForm
from .models import UserProfile


def home(request):
    # Send users to the right first page based on authentication state.
    if request.user.is_authenticated:
        return redirect("profile")
    return redirect("account_login")


@login_required
def profile_upsert(request):
    # Avoid creating an empty profile row on GET; create only on valid POST.
    profile = UserProfile.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            saved = form.save(commit=False)
            # Ensure profile ownership always matches the logged-in user.
            saved.user = request.user
            saved.save()
            messages.success(request, "Profile saved successfully.")
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        "profiles/profiles_form.html",
        {"form": form, "profile": profile},
    )
#Handles adding a new blood pressure reading.

@login_required
def add_bp_reading(request):

    if request.method == "POST":
        form = BloodPressureReadingForm(request.POST)
        if form.is_valid():
            reading = form.save(commit=False)
            reading.user = request.user
            reading.save()
            messages.success(request, "Blood pressure reading saved!")
            return redirect("profile")
    else:
        form = BloodPressureReadingForm()

    return render(request, "profiles/bp_reading_form.html", {"form": form})