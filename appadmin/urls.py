from django.urls import path, include
from . import views

app_name = 'adm'
urlpatterns = [
    path('', views.index, name='admin_index'),
    path('editar_partida/<int:pk>/', views.editar_partida, name='editar_partida'),
    path('edita/<int:pk>', views.editar, name='edita'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]