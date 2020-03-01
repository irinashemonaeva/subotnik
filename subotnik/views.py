from django.shortcuts import render

# Create your views here.
def login_popup (request):
    return render (request, 'login_popup.html')

def index (request):
    return render (request, 'index.html')

def sidebar (request):
    return render (request, 'sidebar.html')

