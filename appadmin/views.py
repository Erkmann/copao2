from django.shortcuts import render
from apptimes.models import Partida
from apptimes.models import Time
from apptimes.models import Jogador
from django.core.paginator import Paginator


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

def editar_partida(request, pk1, pk2):
    if request.method == 'GET':
        time1 = Time.objects.get(id=pk1)
        time2 = Time.objects.get(id=pk2)
        jogadores_t1 = Jogador.objects.filter(id_time=pk1)
        jogadores_t2 = Jogador.objects.filter(id_time=pk2)
        context = {'time1': time1, 'time2': time2, 'jogadores_t1': jogadores_t1, 'jogadores_t2': jogadores_t2}
        return render(request, 'appadmin/edita_partida.html', context)
