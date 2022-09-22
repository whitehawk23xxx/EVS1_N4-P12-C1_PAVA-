from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def displayApp2(request):
    return HttpResponse("<h1>ya que logro llegar aquí ¡¡¡¡Felicidades¡¡¡¡</h1>")
                        
def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)