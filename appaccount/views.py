from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from apptimes.models import Usuario, Time, Jogador
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
    usuario = Usuario.objects.get(id=pk)
    time = Time.objects.get(admin_time=usuario.id)

    jogadores = Jogador.objects.filter(id_time=time.id)
    jogadoresTodos = Jogador.objects.exclude(id_time=time.id)

    context = {'usuario': usuario, 'time': time, 'jogadoresMeu': jogadores, 'jogadoresTodos': jogadoresTodos}
    return render(request, 'appaccount/usuario.html', context)