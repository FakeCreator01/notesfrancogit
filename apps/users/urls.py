from django.urls import path, include
from .views import *

urlpatterns = [
    path("login/", Login.as_view(), name="login_view"),
    path("logout/", LogoutView.as_view(), name="logout_view"),
    path("signup/", Signup.as_view(), name="signup")
]
