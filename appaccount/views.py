from datetime import date
from itertools import count
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm
from apptimes.models import Usuario, Time, Jogador, Notificacao, Transferencia, TransferenciaJogador, JogadorNaPartida, PartidasEditadas, Partida
from django.contrib.auth.models import User
from django.db.models import Q
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
    jogadoresTodos = Jogador.objects.exclude(id_time=time.id).order_by('-id_time')
    notificacoes = Notificacao.objects.filter(id_receptor=pk, respondida=0)

    jogs = []

    notificacoesEnviadas = Notificacao.objects.filter(id_enviador=pk, respondida=0)
    for jog in jogadoresTodos:
        n = 0
        for notE in notificacoesEnviadas:
            if jog.id == notE.id_jogador.id:
                n += 1
        if n == 0:
            if jog.id_time == None:
                timeO = Time(id=0, logo='alow', pontos=0, cor='grey', saldo_gols=0, vitoria=0, admin_time=None)
                jog.id_time = timeO
            jogs.append(jog)

    countT = len(jogs)
    for notI in notificacoes:
        timeAdmin = Time.objects.get(admin_time=notI.id_enviador)
        notI.time = timeAdmin
    countN = len(notificacoes)

    context = {'usuario': usuario, 'time': time, 'jogadoresMeu': jogadores, 'jogadoresTodos': jogs, 'totalJ': countJ, 'totalT': countT, 'times': times, 'notificacoes':notificacoes, 'countN': countN}
    return render(request, 'appaccount/usuario.html', context)

def confirmacao_solicitar(request, jogador, time_solicitante, time_solicitado, pk):
    jogador = Jogador.objects.get(id=jogador)
    if time_solicitado == 0:
        context = {'jogador': jogador, 'time_solicitante': time_solicitante, 'time_solicitado': 0, 'pk': pk}
    else:
        context = {'jogador': jogador, 'time_solicitante': time_solicitante, 'time_solicitado': time_solicitado, 'pk': pk}
    return render(request, 'appaccount/confirma_pedido.html', context)


def solicitar(request, jogador, time_solicitante, time_solicitado, pk):
    if time_solicitado != 0:
        time_solicitante = Time.objects.get(id=time_solicitante)
        jogadoresTimeS = Jogador.objects.filter(id=time_solicitante.id)
        usuario = User.objects.get(id=pk)
        jogador = Jogador.objects.get(id=jogador)
        time_solicitado = Time.objects.get(id=time_solicitado)
        countJogadores = len(jogadoresTimeS)

        if countJogadores >= 13:
            return 'Nao pode solicitar pcausa do numero de jogadores ja cadastrados no time'
        else:
            notificacao = Notificacao.objects.create(id_receptor=time_solicitado.admin_time, id_enviador=time_solicitante.admin_time, id_jogador=jogador)
            return account(request, pk)
    else:
        time_solicitante = Time.objects.get(id=time_solicitante)
        jogadoresTimeS = Jogador.objects.filter(id=time_solicitante.id)
        jogador = Jogador.objects.get(id=jogador)
        countJogadores = len(jogadoresTimeS)

        if countJogadores >= 13:
            return 'Nao pode solicitar pcausa do numero de jogadores ja cadastrados no time'
        else:
            jogador.id_time = time_solicitante
            jogador.save()
            return account(request, pk)

def aceitar_transferencia(request, jogador, pk, time_solicitante, notificacao_id):
    jogador = Jogador.objects.get(id=jogador)
    time_vendedor = jogador.id_time
    time_solicitante = Time.objects.get(id=time_solicitante)
    transferencia = Transferencia.objects.create(time_vendedor=time_vendedor, time_comprador=time_solicitante)
    transferenciaJogador = TransferenciaJogador.objects.create(jogador = jogador, transferencia = transferencia)
    notificacao = Notificacao.objects.get(id=notificacao_id)
    notificacao.respondida = 1
    notificacao.save()

    timeAdminSolicitante = Time.objects.get(admin_time=time_solicitante.admin_time)
    notificacaoDeletar = Notificacao.objects.filter(id_jogador=jogador).exclude(id_enviador=timeAdminSolicitante.admin_time)

    for notDel in notificacaoDeletar:
        notDel.delete()

    jogador.id_time = time_solicitante
    jogador.save()

    partidasDoJogador = JogadorNaPartida.objects.filter(jogador = jogador)

    data = date.today()

    print(data)

    for p in partidasDoJogador:
        print(p.partida.data)
        if p.partida.data >= data:
            p.delete()

    partidasDoTime = Partida.objects.filter(Q(id_time_mandante=time_solicitante) | Q(id_time_visitante=time_solicitante))

    for p in partidasDoTime:
        if p.data > data:
            print(p.data)
            jogador_partida = JogadorNaPartida(jogador = jogador, partida = p)
            jogador_partida.save()

    return account(request, pk)

def recusar_transferencia(request, notificacao_id, pk):
    notificacao = Notificacao.objects.get(id=notificacao_id)
    notificacao.respondida = 1
    notificacao.save()

    return account(request, pk)

def confirmar_dispensar(request, pk, admin):
    jogador = Jogador.objects.get(id=pk)
    context = {'jogador': jogador, 'admin': admin}
    return render(request, 'appaccount/confirma_dispensar.html', context)

def dispensar(request, pk, admin):
    jogador = Jogador.objects.get(id=pk)
    jogador.id_time = None
    jogador.save()
    return account(request, admin)