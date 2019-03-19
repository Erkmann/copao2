from django.shortcuts import render
from apptimes import models as ModelsAppTimes

app_name = 'index'
def index(request):
    times = ModelsAppTimes.Time.objects.all()
    context = {'name': 'Index', 'times': times}
    return render(request, 'copaoifc/index.html',context)

def login(request):
    context = {'name' : 'Login'}
    return render(request, 'copaoifc/index.html', context)

