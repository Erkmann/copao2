from django.shortcuts import render
from apptimes.models import Time, Jogador, Transferencia, TransferenciaJogador
from datetime import datetime


# Create your views here.

def index(request):
    transferencias = TransferenciaJogador.objects.all()
    context = {'transferencias': transferencias}
    return render(request, 'apptransferencias/transferencias.html', context)