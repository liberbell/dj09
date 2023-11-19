from django.urls import path
from .views

urlpatterns = [
    path("signup/", signupfunc, name="signup"),
]
