from django.contrib import admin
from django.urls import path
from .views import login_attempt
from authentication import views

urlpatterns = [
    path("", views.login_attempt, name='login_attempt'),
]