from django.shortcuts import render
from apptimes.models import Time


def index(request):
    times = Time.objects.all().order_by('-pontos', '-vitoria', '-saldo_gols')
    context = {'times': times, }
    return render(request, 'appclassificacao/classificacao.html', context)
