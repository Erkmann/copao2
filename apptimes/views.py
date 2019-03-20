from django.shortcuts import render
from . models import Time, Jogador, Partida
from django.db.models import Q

def index(request):
   times =  Time.objects.all()
   context = {'times': times}
   return render(request, 'apptimes/times.html', context)

def time(request, pk):
   time = Time.objects.get(id=pk)
   jogadores = Jogador.objects.filter(id_time=pk)
   partidas = Partida.objects.filter(Q(id_time_mandante=pk) | Q(id_time_visitante=pk))
   context = {'time': time, 'jogadores': jogadores, 'partidas': partidas}
   return render(request, 'apptimes/time.html', context)
