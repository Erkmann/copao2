from django.urls import path, include
from . import views
from apptimes import views as times
from apptimes import urls as time
from appclassificacao import urls as classificacao
from appartilheiros import urls as artilheiros


urlpatterns = [
    path('', views.index, name='index'),
    path('times/', times.index , name='times'),
    path('login/', views.login, name='login'),
    path('', include(time, namespace='time')),
    path('classificacao/', include(classificacao, namespace='classificacao')),
    path('artilheiros/', include(artilheiros, namespace='artilheiros')),
]