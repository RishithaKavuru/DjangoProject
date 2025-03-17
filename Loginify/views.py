from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import UserDetails

# Create your views here.
def demo(request):
    return HttpResponse("Hello World!")

def sign_up(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if UserDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect("signup")

        user = UserDetails(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect("login")

    return render(request, 'Loginify/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserDetails.objects.get(email=email, password=password)
            messages.success(request, f"Welcome, {user.username}!")
            return render(request, "Loginify/success.html", {"username": user.username})
        except UserDetails.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("login")

    return render(request, 'Loginify/login.html')

