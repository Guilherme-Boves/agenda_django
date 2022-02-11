from xml.dom.pulldom import PROCESSING_INSTRUCTION
from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def evento(request, titulo_evento):    
    return HttpResponse('<h1>Seu evento é: {}</h1>'.format(Evento.objects.get(titulo = titulo_evento)))