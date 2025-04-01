from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, "index.html", {"base_template": base_template})

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            messages.error(request, "Your password and confirm password do not match!")
            return render(request, 'login.html')  # Redirects to the login page with register section

        if not validate_password(pass1):
            messages.error(request, "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return render(request, 'login.html')  # Redirects to the login page with register section

        # Check if username or email already exists
        
        # Create user
        user = User.objects.create_user(username=uname, email=email, password=pass1)
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')  # Redirects to the login page

    return render(request, 'login.html')  # Redirects to the login page with register section


def validate_password(password):
    """ Validates password strength """
    if (
        len(password) < 8 or
        not any(char.isupper() for char in password) or
        not any(char.islower() for char in password) or
        not any(char.isdigit() for char in password) or
        not any(char in '!@#$%^&*()-_=+[]{};:,.<>?/' for char in password)
    ):
        return False
    return True

# Login verification

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Attempting login: Username = {username}, Password = {password}")

        try:
            user = User.objects.get(username=username)
            print("User found:", user)
            print("Stored password (hashed):", user.password)
            print("Check password result:", user.check_password(password))
        except User.DoesNotExist:
            print("User does not exist")
            return render(request, 'login.html', {'error': "Username does not exist!"})

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            print("Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password!")
            print("Authentication failed!")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')

def contact(request): 
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, "contact.html", {"base_template": base_template})

def blogs(request):
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, "blogs.html", {"base_template": base_template})

def history(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, "history.html", {"base_template": base_template})

def recommendations(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, "recommendations.html", {"base_template": base_template})

def symptoms(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'symptoms.html', {"base_template": base_template})

def health(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'health.html', {"base_template": base_template})

def myths(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'myths.html', {"base_template": base_template})

def personal_stories(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'personal_stories.html', {"base_template": base_template})

def research_innovations(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'research_innovations.html', {"base_template": base_template})

def cardiac_rehab(request):
    print(request.user.is_authenticated)
    base_template = "base1.html" if request.user.is_authenticated else "base.html"
    return render(request, 'cardiac_rehab.html', {"base_template": base_template})
#2d echo

from django.shortcuts import render

def predict_cardiac_arrest(ejection_fraction, lv_edd, pap, mitral_regurgitation, pericardial_effusion):
    """Threshold-based logic for cardiac arrest prediction"""
    if (ejection_fraction < 40 or lv_edd > 65 or pap > 30 or 
        mitral_regurgitation == "Severe" or pericardial_effusion == "Present"):
        return "High Risk of Cardiac Arrest 🚨"
    else:
        return "Low Risk of Cardiac Arrest ✅"

def predict_view(request):
    if request.method == "POST":
        # Get form data
        ejection_fraction = float(request.POST.get("ejection_fraction"))
        lv_edd = float(request.POST.get("lv_edd"))
        pap = float(request.POST.get("pap"))
        mitral_regurgitation = request.POST.get("mitral_regurgitation")
        pericardial_effusion = request.POST.get("pericardial_effusion")

        # Make prediction
        result = predict_cardiac_arrest(ejection_fraction, lv_edd, pap, mitral_regurgitation, pericardial_effusion)

        # Render with result
        return render(request, "2decho.html", {"result": result})

    return render(request, "2decho.html")



#wpr blood test


def calculate_wpr(request):
    result = None

    if request.method == "POST":
        try:
            wbc_count = int(request.POST.get('wbc_count'))
            platelet_count = int(request.POST.get('platelet_count'))

            if platelet_count > 0:  # Avoid division by zero
                wpr = wbc_count / platelet_count  

                # Determine Risk Level
                if wpr < 0.025:
                    risk_level = "✅ Low Risk - Normal heart function"
                elif 0.025 <= wpr < 0.05:  # Now WPR=0.05 will be High Risk
                    risk_level = "⚠️ Moderate Risk - Possible early heart disease"
                else:  # WPR ≥ 0.05
                    risk_level = "🚨 High Risk - Increased heart attack risk"


                result = f"WPR Value: {wpr:.5f} | Risk Level: {risk_level}"
            else:
                result = "❌ Error: Platelet count must be greater than zero."

        except ValueError:
            result = "❌ Error: Please enter valid numerical values."

    return render(request, "wpr_form.html", {"result": result})


#lifestyle predict

import os
import joblib
import numpy as np
from django.shortcuts import render, redirect



model_path = "myproject/ml_models/heart_attack_model.joblib"  # Update the path if needed
ml_model = joblib.load(model_path)


import joblib
import numpy as np
from django.shortcuts import render, redirect

# Load the trained model and scaler
model = joblib.load("myproject/ml_models/heart_attack_model.joblib")
scaler = joblib.load("myproject/ml_models/scaler.joblib")

def predict_heart_attack(request):
    if request.method == "POST":
        try:
            # Extracting input data
            age = float(request.POST.get("age"))
            cholesterol = float(request.POST.get("cholesterol"))
            blood_pressure = request.POST.get("blood_pressure")
            heart_rate = float(request.POST.get("heart_rate"))
            diabetes = int(request.POST.get("diabetes"))
            family_history = int(request.POST.get("family_history"))
            smoking = int(request.POST.get("smoking"))
            obesity = int(request.POST.get("obesity"))
            alcohol = int(request.POST.get("alcohol"))
            exercise_hours = float(request.POST.get("exercise_hours"))
            diet = int(request.POST.get("diet"))
            previous_heart_problems = int(request.POST.get("previous_heart_problems"))
            medication_use = int(request.POST.get("medication_use"))
            stress_level = float(request.POST.get("stress_level"))
            sedentary_hours = float(request.POST.get("sedentary_hours"))
            bmi = float(request.POST.get("bmi"))
            triglycerides = float(request.POST.get("triglycerides"))
            physical_activity = int(request.POST.get("physical_activity"))
            sleep_hours = float(request.POST.get("sleep_hours"))

            # Convert blood pressure (sys/dia)
            systolic, diastolic = map(float, blood_pressure.split("/"))

            # Prepare input data as a numpy array
            input_data = np.array([
                age, cholesterol, systolic, diastolic, heart_rate, diabetes,
                family_history, smoking, obesity, alcohol, exercise_hours, diet,
                previous_heart_problems, medication_use, stress_level, sedentary_hours,
                bmi, triglycerides, physical_activity, sleep_hours
            ]).reshape(1, -1)

            # Scale input data
            input_data_scaled = scaler.transform(input_data)

            # Make prediction
            prediction = model.predict(input_data_scaled)

            # Convert prediction to readable output
            risk = "High" if prediction[0] == 1 else "Low"

            # Redirect to results page with prediction data
            return render(request, "result.html", {"risk": risk})

        except Exception as e:
            return render(request, "result.html", {"error": str(e)})

    return render(request, "predict.html")
