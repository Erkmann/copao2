from django.shortcuts import render


def index(request):
    context = {'name': 'Index'}
    return render(request, 'copaoifc/index.html',context)

def login(request):
    context = {'name' : 'Login'}
    return render(request, 'copaoifc/index.html', context)