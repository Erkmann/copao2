from django.urls import path, include
from . import views

app_name = 'partidas'
urlpatterns = [
    path('', views.index, name='partidas_index'),
]