from datetime import datetime
from itertools import count

from django.shortcuts import render
from apptimes.models import Partida, Time, Jogador, JogadorNaPartida, PartidasEditadas
from django.core.paginator import Paginator
from appaccount.forms import PartidaForm
from django.db.models import Q


# Create your views here.

def index(request):
    partidas = Partida.objects.all().order_by('data')

    paginator = Paginator(partidas, 3)  # Show 15 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    paginas = []

    for numero in range(1, contacts.paginator.num_pages + 1):
        paginas.append(numero)

    context = {'partidas': contacts, 'paginas': paginas}

    return render(request, 'appadmin/admin.html', context)

def editar_partida(request, pk):
    if request.method == 'GET':
        partida = Partida.objects.get(id = pk)
        time1 = Time.objects.get(id=partida.id_time_mandante.id)
        time2 = Time.objects.get(id=partida.id_time_visitante.id)
        jogadores_t1 = Jogador.objects.filter(id_time=time1.id)
        jogadores_t2 = Jogador.objects.filter(id_time=time2.id)

        jogadoresJaEditados = JogadorNaPartida.objects.filter(partida=partida.id)
        jogadoresEditados = []

        jogadoresJaEditados_t1 = []
        jogadoresJaEditados_t2 = []

        jogadoresQueJogaram = []
        for jogador in jogadoresJaEditados:
            jogadoresQueJogaram.append(jogador.jogador)

        for jogador in jogadores_t1:
            if jogador in jogadoresQueJogaram:
                for jogE in jogadoresJaEditados:
                    if jogador.id == jogE.jogador.id:
                        jogadoresEditados.append(jogE)
            else:
                j = JogadorNaPartida(partida=partida, jogador=jogador)
                jogadoresEditados.append(j)
                j.save()



        for jogador in jogadores_t2:
            if jogador in jogadoresQueJogaram:
                for jogE in jogadoresJaEditados:
                    if jogador == jogE.jogador:
                        jogadoresEditados.append(jogE)
            else:
                j = JogadorNaPartida(partida=partida, jogador=jogador)
                jogadoresEditados.append(j)
                j.save()

        for jogador in jogadoresEditados:
            if jogador.jogador.id_time.id == time1.id:
                jogadoresJaEditados_t1.append(jogador)
            else:
                jogadoresJaEditados_t2.append(jogador)

        context = {'jogadores_t1': jogadoresJaEditados_t1, 'jogadores_t2': jogadoresJaEditados_t2, 'time1': time1, 'time2': time2, 'jogadorNaPartida': jogadoresEditados, 'partida': partida}
        return render(request, 'appadmin/edita_partida.html', context)

def salvarEditar(request, partida, jogadoresNasPartidas, partidasEditadas, timeA, timeB):
    for p in request.POST:
        if p == 'csrfmiddlewaretoken':
            pass
        elif p[1] == 'o':
            jP = ''
            for num in p:
                if num != 'g' and num != 'o':
                    jP += num

            jogadorP = JogadorNaPartida.objects.get(id=jP)

            ca = 'ca' + jP
            for a in request.POST:
                if a == ca:
                    ca = request.POST[ca]

            go = 'go' + jP
            for a in request.POST:
                if a == go:
                    go = request.POST[go]

            cv = 'cv' + jP
            for a in request.POST:
                if a == cv:
                    cv = request.POST[cv]

            attJogadorP = JogadorNaPartida(id=jP, jogador=jogadorP.jogador, partida=jogadorP.partida, gols=go,
                                           cartoes_amarelos=ca, cartoes_vermelhos=cv)
            if jogadorP not in jogadoresNasPartidas:
                jogadoresNasPartidas.append(attJogadorP)

    golsTimeA = 0
    golsTimeB = 0

    for jog in jogadoresNasPartidas:
        golsJog = jog.gols
        if jog.jogador.id_time == timeA:
            golsTimeA += int(golsJog)
        else:
            golsTimeB += int(golsJog)

        cartaoA = jog.cartoes_amarelos
        cartaoV = jog.cartoes_vermelhos

        if int(golsJog) > 0:
            jog.jogador.gols += int(golsJog)

        if int(cartaoA) > 0:
            jog.jogador.cartao_amarelo += int(cartaoA)

        if int(cartaoV) > 0:
            jog.jogador.cartao_vermelho += int(cartaoV)

        jog.jogador.save()
        jog.save()

    partida.gols_timeA = golsTimeA
    partida.gols_timeB = golsTimeB

    if golsTimeA > golsTimeB:
        timeA.pontos += 3
        timeA.vitoria += 1
    elif golsTimeB > golsTimeA:
        timeB.pontos += 3
        timeB.vitoria += 1
    else:
        timeA.pontos += 1
        timeB.pontos += 1

    timeA.saldo_gols = timeA.saldo_gols + golsTimeA
    timeA.saldo_gols = timeA.saldo_gols - golsTimeB
    timeB.saldo_gols = timeB.saldo_gols + golsTimeB
    timeB.saldo_gols = timeB.saldo_gols - golsTimeA

    timeA.save()
    timeB.save()

    partida.save()

    partidasEditadas.editada = 1
    partidasEditadas.save()

    return 1

def editar(request, pk):
    partida = Partida.objects.get(id=pk)
    timeA = partida.id_time_mandante
    timeB = partida.id_time_visitante
    partidasEditadas = PartidasEditadas.objects.get(partida = partida)

    jogadoresNasPartidas = []

    if partidasEditadas.editada == 0:
        salvarEditar(request, partida, jogadoresNasPartidas, partidasEditadas, timeA, timeB)
        return render(request, 'appadmin/exibe_partida.html')

    else:
        jogadoresPartidas = JogadorNaPartida.objects.filter(partida = partida)

        golsA = 0
        golsB = 0
        for j in jogadoresPartidas:
            if j.jogador.id_time == partida.id_time_mandante:
                golsA = golsA + j.gols
            else:
                golsB = golsB + j.gols

            j.jogador.gols = j.jogador.gols - j.gols
            j.jogador.cartao_amarelo = j.jogador.cartao_amarelo - j.cartoes_amarelos
            j.jogador.cartao_vermelho = j.jogador.cartao_vermelho - j.cartoes_vermelhos
            j.jogador.save()

        if golsA > golsB:
            partida.id_time_mandante.pontos = partida.id_time_mandante.pontos - 3
            partida.id_time_mandante.vitoria = partida.id_time_mandante.vitoria - 1
        elif golsB > golsA:
            partida.id_time_visitante.pontos = partida.id_time_visitante.pontos - 3
            partida.id_time_visitante.vitoria = partida.id_time_visitante.vitoria - 1
        else:
            partida.id_time_visitante.pontos = partida.id_time_visitante.pontos - 1
            partida.id_time_mandante.pontos = partida.id_time_mandante.pontos - 1

        partida.id_time_mandante.saldo_gols = partida.id_time_mandante.saldo_gols - golsA
        partida.id_time_mandante.saldo_gols = partida.id_time_mandante.saldo_gols + golsB

        partida.id_time_visitante.saldo_gols = partida.id_time_visitante.saldo_gols - golsB
        partida.id_time_visitante.saldo_gols = partida.id_time_visitante.saldo_gols + golsA

        partida.id_time_mandante.save()
        partida.id_time_visitante.save()

        partida.save()

        salvarEditar(request, partida, jogadoresNasPartidas, partidasEditadas, timeA, timeB)

    return render(request, 'appadmin/exibe_partida.html')

def cadastrar(request):
    times = Time.objects.all()

    for time in times:
        jogadores = Jogador.objects.filter(id_time = time)
        partidas = Partida.objects.filter(Q(id_time_mandante=time) | Q(id_time_visitante=time))

        for partida in partidas:
            for jogador in jogadores:
                jogadorNaPartida = JogadorNaPartida.objects.filter(partida = partida, jogador = jogador)

                lista = []
                for j in jogadorNaPartida:
                    lista.append(j)

                if len(lista) > 0:
                    pass
                else:
                    jog = JogadorNaPartida(jogador = jogador, partida = partida)
                    jog.save()

    return render(request, 'appadmin/exibe_partida.html')