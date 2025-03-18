from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import UserDetails
from .Serializers import UserDetailsSerializer
from django.views.decorators.csrf import csrf_exempt
import json

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

#Get all user details view:
def all_data(request):
    if request.method == "GET":
        users = UserDetails.objects.all()
        serialized_data = UserDetailsSerializer(users,many=True)
        return JsonResponse(serialized_data.data, safe=False)

#Get a single user using by email view:  
def single_user(request, email):
    if request.method == "GET":
        try:
            user = UserDetails.objects.get(email=email)
            serialized_data = UserDetailsSerializer(user)
            return JsonResponse({
                "success": True,
                "Data": serialized_data.data
                }, status= 200)
        
        except Exception as e:
            return JsonResponse({ 
                "success": False,
                "error": str(e)
                }, status= 400)

#Update user details
@csrf_exempt
def update_user(request, email):
    if request.method == "PUT":
        try:
            user = UserDetails.objects.get(email=email)
            input_data = json.loads(request.body)

            input_data.pop("email", None)

            serialized_data = UserDetailsSerializer(user, data=input_data)
            if serialized_data.is_valid():
                serialized_data.save()

            return JsonResponse({
                "success": True,
                "message": "Data updated successfully",
                "Data": serialized_data.data
            }, status = 200)
        
        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status = 400)

#Delete User
@csrf_exempt
def delete_user(request, email):
    if request.method == "DELETE":
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({
                "success": True,
                "message": "User deleted successfully"
                }, status = 200)
        
        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status = 400)