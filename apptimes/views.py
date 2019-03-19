from django.shortcuts import render
from . models import Time

def index(request):
   times =  Time.objects.all()
   context = {'times': times}
   return render(request, 'apptimes/times.html', context)

def time(request, pk):
   time = Time.objects.get(id=pk)
   context = {'time': time}
   return render(request, 'apptimes/time.html', context)
