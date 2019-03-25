from itertools import count
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from apptimes.models import Usuario, Time, Jogador, Notificacao
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['nome_usuario']
            password = form.cleaned_data['senha']
            user = authenticate(nome_usuario=username, senha=password)
            login(request, user)
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def account(request, pk):
    usuario = User.objects.get(id=pk)
    time = Time.objects.get(admin_time=usuario.id)
    times = Time.objects.exclude(id = time.id)

    jogadores = Jogador.objects.filter(id_time=time.id)
    countJ = len(jogadores)
    jogadoresTodos = Jogador.objects.exclude(id_time=time.id)
    countT = len(jogadoresTodos)
    notificacoes = Notificacao.objects.filter(id_receptor=pk)
    countN = len(notificacoes)

    context = {'usuario': usuario, 'time': time, 'jogadoresMeu': jogadores, 'jogadoresTodos': jogadoresTodos, 'totalJ': countJ, 'totalT': countT, 'times': times, 'notificacoes':notificacoes, 'countN': countN}
    return render(request, 'appaccount/usuario.html', context)