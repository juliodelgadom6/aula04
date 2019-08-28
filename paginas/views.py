from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def paginaInicioView(request):
    return HttpResponse('<h1>Benvindo ao curso de E-commerce!</h1>')