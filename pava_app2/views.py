from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def displayApp2(request):
    return HttpResponse("<h1>Gracias por Partipar en esta segunda vista</h1>")
                        
