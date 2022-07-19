from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'website_startapp/index.html')

def add_expense(request):
    return render(request, 'website_startapp/add_expense.html')
