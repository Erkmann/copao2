# django.contrib.auth.urls

from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('logout/', include('django.contrib.auth.urls'),name='logout')
]