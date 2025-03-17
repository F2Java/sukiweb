from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def index(request):
    context = {
        'welcome_text': 'WELCOME TO SUPER SUKI',
    }
    return render(request, 'index.html', context)

def home(request):
    context = {
        'welcome_text': 'Welcome to Home of Super Suki',
    }
    return render(request, 'home.html', context)

def ourmenu(request):
    context = {
        'welcome_text': 'Welcome to Menu of Super Suki',
    }
    return render(request, 'ourmenu.html', context)

def ourloc(request):
    context = {
        'welcome_text': 'Welcome to Our Location of Super Suki',
    }
    return render(request, 'ourloc.html', context)

def busops(request):
    context = {
        'welcome_text': 'Welcome to Business-Opportunities of Super Suki',
    }
    return render(request, 'busops.html', context)

def contact(request):
    context = {
        'welcome_text': 'Welcome to Contact of Super Suki',
    }
    return render(request, 'contact.html', context)



    
    
    

    

    
    
    


    
    
    