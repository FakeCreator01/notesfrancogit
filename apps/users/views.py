from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

class Login(LoginView):
	template_name = "usuarios/login.html"

class Signup(CreateView):
	template_name = "usuarios/signup.html"
	form_class = UserCreationForm #form creado por django
	success_url = reverse_lazy("usuarios:login_view")


