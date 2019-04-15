from django.shortcuts import render
from apptimes.models import Partida, Time, Jogador, JogadorNaPartida
from django.core.paginator import Paginator
from appaccount.forms import PartidaForm


# Create your views here.

def index(request):
    partidas = Partida.objects.all().order_by('-data')

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



        for jogador in jogadores_t2:
            if jogador in jogadoresQueJogaram:
                for jogE in jogadoresJaEditados:
                    if jogador == jogE.jogador:
                        jogadoresEditados.append(jogE)
            else:
                j = JogadorNaPartida(partida=partida, jogador=jogador)
                jogadoresEditados.append(j)



        for jogador in jogadoresEditados:
            if jogador.jogador.id_time.id == time1.id:
                jogadoresJaEditados_t1.append(jogador)
            else:
                jogadoresJaEditados_t2.append(jogador)

        context = {'jogadores_t1': jogadoresJaEditados_t1, 'jogadores_t2': jogadoresJaEditados_t2, 'time1': time1, 'time2': time2, 'jogadorNaPartida': jogadoresEditados, 'partida': partida}
        return render(request, 'appadmin/edita_partida.html', context)

def editar(request, pk):
    partida = Partida.objects.get(id = pk)

    jogadoresNasPartidas = []


    for p in request.POST:
        if p == 'csrfmiddlewaretoken':
            pass
        elif p[1] == 'o':
            jP = p[2]
            jogadorP = JogadorNaPartida.objects.get(id = jP)

            ca = 'ca' + jP
            for a in request.POST:
                if a == ca:
                    ca = a

            cv = 'cv' + jP
            for a in request.POST:
                if a == cv:
                    cv = a

            attJogadorP = JogadorNaPartida(id = jP, jogador = jogadorP.jogador, partida = jogadorP.partida, gols = p[2], cartoes_amarelos = ca[2], cartoes_vermelhos = cv[2])
            if jogadorP not in jogadoresNasPartidas:
                jogadoresNasPartidas.append(attJogadorP)




    context = {'post': request.POST, 'jogadoresNaPartida': jogadoresNasPartidas}
    return render(request, 'appadmin/exibe_partida.html', context)