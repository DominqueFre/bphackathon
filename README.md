# Blood Pressure Tracker

A simple, clean, and fully responsive Django web application that allows users to record, view, and manage their blood pressure readings.  
The project was built collaboratively during a hackathon and focuses on delivering essential CRUD functionality, user authentication, and a polished Bootstrap‑based UI.

---

## 🚀 Live Site  
**Live Deployment:** *(https://shielded-springs-56275-f2da7cb0bd7a.herokuapp.com/)*  
**GitHub Repository:** *(https://github.com/DominqueFre/bphackathon)*

---

## 📌 Project Overview

Blood Pressure Tracker is a lightweight health‑monitoring tool that enables users to:

- Create and manage a personal health profile  
- Automatically calculate BMI  
- Record blood pressure readings with systolic, diastolic, pulse, arm, and position data  
- View readings in a clean, sortable table  
- Edit or delete readings  
- Access all features through a secure login system powered by Django Allauth  

The goal was to build a functional, accessible, and user‑friendly MVP within a short timeframe.

---

## ✨ Features

### 🔐 Authentication
- User registration, login, logout (Django Allauth)
- Custom‑styled login, signup, and logout pages
- Login required for all profile and reading pages

### 👤 User Profile
- NHS number, age, gender, height, weight
- Automatic BMI calculation
- Profile summary page
- Profile edit page

### ❤️ Blood Pressure Readings
- Add new readings
- Edit existing readings
- Delete readings with confirmation
- View all readings in a Bootstrap table
- Colour‑coded systolic/diastolic values
- Icons for reading position (sitting, standing, prone)

### 🎨 UI & UX
- Fully responsive Bootstrap 5 layout
- Consistent card‑based design
- Clear navigation and call‑to‑action buttons
- FontAwesome icons throughout

---

## 🗂️ Data Model

### **UserProfile**
| Field | Type | Notes |
|-------|------|-------|
| user | OneToOneField | Linked to Django User |
| nhs_number | CharField | Basic validation |
| age | IntegerField | |
| gender | CharField | Choice field |
| height_m | DecimalField | Used for BMI |
| weight_kg | DecimalField | Used for BMI |
| created_at | DateTimeField | Auto timestamp |
| updated_at | DateTimeField | Auto timestamp |

**BMI** is calculated via a model property.

---

### **BloodPressureReading**
| Field | Type | Notes |
|-------|------|-------|
| user | ForeignKey | Linked to Django User |
| systolic | IntegerField | Validated |
| diastolic | IntegerField | Validated |
| pulse | IntegerField | Optional |
| arm | CharField | Choice field |
| position | CharField | Choice field |
| reading_date | DateField | |
| reading_time | TimeField | |
| comment | TextField | Optional |

---

## 🔄 CRUD Functionality

### Profile
- **Create**: First visit to profile edit page  
- **Read**: Profile summary page  
- **Update**: Edit profile  
- **Delete**: Not required for this MVP  

### Blood Pressure Readings
- **Create**: Add reading form  
- **Read**: Reading list table  
- **Update**: Edit reading  
- **Delete**: Delete confirmation page  

All CRUD operations are restricted to the logged‑in user.

---

## 🔒 Security & Authentication

- Django Allauth handles registration, login, logout  
- Login required for all profile and reading views  
- Users can only access their own data  
- CSRF protection enabled  
- Form validation on both client and server side  

---

## 🧪 Automated Testing

Automated tests were written using Django’s built‑in `TestCase` framework.

### ✔ Model Tests
- BMI calculation  
- String representations  
- Reading creation  

### ✔ Form Tests
- Valid and invalid profile form data  
- Valid and invalid reading form data  

### ✔ View Tests
- Login required redirects  
- Correct templates rendered  
- Successful reading creation  
- Profile page loads correctly  

### ✔ Test Result
All tests passed successfully.  
*(Screenshot can be added later if desired.)*

Run tests with:

```
python manage.py test
```

---

## 🧪 Manual Testing

Manual testing was performed on all key user flows:

- Login / Logout  
- Signup  
- Profile creation and editing  
- Adding readings  
- Editing readings  
- Deleting readings  
- Navigation links  
- Form validation  
- Mobile responsiveness  

All functionality behaved as expected.

---

## 🌐 Deployment

The project was deployed to **Heroku** using:

- PostgreSQL database  
- `whitenoise` for static file handling  
- `gunicorn` as the WSGI server  

### Required Config Vars:
- `SECRET_KEY`
- `DEBUG` (set to False)
- `DATABASE_URL`
- `ALLOWED_HOSTS`
- `CLOUDINARY_URL` (if used for media)

### Deployment Steps:
1. Push code to GitHub  
2. Connect Heroku to the repository  
3. Set config vars  
4. Run migrations  
5. Collect static files  
6. Deploy  

---

## 🛠️ Technologies Used

- **Python 3**  
- **Django 5**  
- **Django Allauth**  
- **Bootstrap 5**  
- **Crispy Forms**  
- **FontAwesome**  
- **PostgreSQL**  
- **Heroku**  

---

## 👥 Credits

This project was created collaboratively by:

- **Jordan** — Developer  
- **Dominique**  — Developer  
- **Saikou**  — Developer  
- **Aklak**  — Developer  

---

## 📄 License

This project is for educational purposes and hackathon use.


