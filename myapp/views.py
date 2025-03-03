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