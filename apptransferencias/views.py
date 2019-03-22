from django.shortcuts import render
from apptimes.models import Time, Jogador, Transferencia
from datetime import datetime


# Create your views here.

def index(request):
    transferencia = Transferencia.objects.all()
    context = {'transferencias': transferencia}
    return render(request, 'apptransferencias/transferencias.html', context)