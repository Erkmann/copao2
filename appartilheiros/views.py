from django.shortcuts import render
from django.core.paginator import Paginator
from apptimes.models import Jogador

# Create your views here.

def index(request):
    jogadores = Jogador.objects.all().order_by('-gols')

    pos = 1

    for jogador in jogadores:
        jogador.pos = pos
        pos += 1

    paginator = Paginator(jogadores, 15)  # Show 15 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {'jogadores': contacts}
    return render(request, 'appartilheiros/artilheiros.html', context)