from xml.dom.pulldom import PROCESSING_INSTRUCTION
from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from core.models import Evento

# Create your views here.

def evento(request, titulo_evento):    
    return HttpResponse('<h1>Seu evento é: {}</h1>'.format(Evento.objects.get(titulo = titulo_evento)))

# def index(request):
#     return redirect('/agenda/')

def listaEventos(request):
    # Coleta os eventos do usuário que está logado
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)