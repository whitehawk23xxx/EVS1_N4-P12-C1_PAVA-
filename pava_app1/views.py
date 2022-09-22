from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
from django.http  import HttpResponse
import datetime



# Create your views here.


def display(request):
    return HttpResponse("<h1>🚵‍♂️🚵‍♂️🚵‍♂️🔻🔻 Hola espero que se encuentren muy bien🔻🔻🚵 🚵 🚵  </h1><h2>💘 💘 💘 💘 espero que se encuentren bien💘 💘 💘 💘 </h2>")


def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b> Fecha y Hora Actual: </b>" + str(dt)
    return HttpResponse(s)
