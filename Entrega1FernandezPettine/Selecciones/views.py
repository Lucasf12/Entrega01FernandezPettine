from django.contrib import admin
from django.shortcuts import render
from .models import Selecciones


# Create your views here.
def home(request):
    return render(request, 'home.html', context{})

def primera_ronda(request):
    return render(request, 'home.html')