from django.urls import path
from . import views

from django.views.decorators.csrf import csrf_exempt

#Defining the path for this app, need to configure this to the main url routing
urlpatterns = [
    path('', views.index, name="website_startapp"),
    path('add-expense', views.add_expense, name="website_startapp") #add_expense is created in views.py

]