from django.shortcuts import render
from apptimes.models import Time


app_name = 'index'
def index(request):
    times = Time.objects.all()
    context = {'name': 'Index', 'times': times}
    return render(request, 'copaoifc/index.html', context)

def login(request):
    context = {'name' : 'Login'}
    return render(request, 'copaoifc/index.html', context)

