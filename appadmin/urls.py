from django.urls import path, include
from . import views

app_name = 'adm'
urlpatterns = [
    path('', views.index, name='admin_index'),
    path('editar_partida/<int:pk1>/<int:pk2>', views.editar_partida, name='editar_partida')
]