from django.shortcuts import render
from apptimes.models import Partida
from django.core.paginator import Paginator

def index(request):
    partidas = Partida.objects.all().order_by('-data')

    paginator = Paginator(partidas, 3)  # Show 15 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {'partidas': contacts}

    return render(request, 'apppartidas/partidas.html', context)