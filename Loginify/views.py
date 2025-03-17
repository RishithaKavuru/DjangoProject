from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
    return HttpResponse("Hello World!")

def sign_up(request):
    return render(request, 'Loginify/index.html')

def login(request):
    return render(request, 'Loginify/login.html')

