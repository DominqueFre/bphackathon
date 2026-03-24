# bphackathon
a simple administrative application for the recording of blood pressure readings

## Table of Contents
-[todelete](#todelete)
-[Introduction](#introduction)
-[Initial steps for setup and deployment](#initial-steps-for-setup-and-deployment)
    -[Steps for Django Framework setup](#steps-for-django-framework-setup)
    -[Steps for deployment](#steps-for-deployment) 
-[Learning Objectives](#learning-objectives)
-[AI Usage](#ai-usage)
-[Supporting documentation](#supporting-documentation)
-[Sources](#sources)


# todelete
To deletevfrom readme after/if used
<style>
@import url('https://fonts.googleapis.com/css2?family=Anonymous+Pro:ital,wght@0,400;0,700;1,400;1,700&display=swap');
</style>
.anonymous-pro-regular {
  font-family: "Anonymous Pro", monospace;
  font-weight: 400;
  font-style: normal;
}

.anonymous-pro-bold {
  font-family: "Anonymous Pro", monospace;
  font-weight: 700;
  font-style: normal;
}

.anonymous-pro-regular-italic {
  font-family: "Anonymous Pro", monospace;
  font-weight: 400;
  font-style: italic;
}

.anonymous-pro-bold-italic {
  font-family: "Anonymous Pro", monospace;
  font-weight: 700;
  font-style: italic;
}

Font awesome
fa-solid fa-heart-pulse      	- for sitting readings  - default
fa-solid fa-bed-pulse		- for prone readings
fa-solid fa-person		- for standing readings



# Introduction
The intention of this application is to record the blood pressure of NHS patients and associated, relevant data.  It is to be created via a hackathon, consisting of a team of four people, namely Aklak, Dominique, Jordan, and Saikou, over the course of three days commencing 4th of March with a deadline of 5pm 26th March 2026.
This hackathon will represent the first sprint in creating such an application, with the aim being to create a functioning application that will allow a user to register and then add their basic data (NHS number, height and weight), before being able to log on as required and create entries for their blood pressure readings, view the history of their blood pressure readings and if necessary edit or delete them.  It is common practice to ignore, for example, the first few readings that are taken due to the data being skewed by abnormal readings, as patients are getting used to using a blood pressure monitor (calculation of averages and automatic removal of outliers is outside the scope of this sprint).
The data to be recorded for blood pressure is systolic pressure in mmHg, diastolic pressure in mmHg, pulse, left or right arm, prone, sitting or standing position and time and date of reading with an additional comment field, for additional non-standard related data.
There will be a general reminder of the various requirements required prior to taking a standard reading, to reiterate the advice and direction provided by health professionals, such as to sit quietly for at least five minutes, and not to have eaten a large meal within the last thirty minutes, and the minimum number of expected readings.  Future functionality could include specific patient direction, where the reading requirements are not standard.
There will be data-entry fields that will prevent null entry and will restrict with a limited ranges for their entries, in order to facilitate analysis and reduce risk of erroneous entries (making it easier for the user to enter the data correctly and therefore taking up less of the health professionals time looking at incorrect readings).
