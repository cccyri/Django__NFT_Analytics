from .views import RegistrationView
from django.urls import path
#to match urls to views


urlpatterns = [
    path('register',RegistrationView.as_view(), name = "register")
]