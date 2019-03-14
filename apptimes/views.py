from django.shortcuts import render
from . models import Time

def index(request):
   times =  Time.objects.all()
   context = {'times': times}
   return render(request, 'apptimes/times.html', context)
