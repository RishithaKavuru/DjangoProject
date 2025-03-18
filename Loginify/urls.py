from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('ph/', views.demo),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.login, name="login"),
    path('all_data/', views.all_data),
    path('single_user/<str:email>/', views.single_user, name="single_user"),
    path('update/<str:email>/', views.update_user, name="update_user"),
    path('delete/<str:email>/', views.delete_user, name="delete_user")
    ]