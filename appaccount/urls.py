# django.contrib.auth.urls
from django.urls import path, include
from . import views

app_name = 'account'
urlpatterns = [
    path('', include('django.contrib.auth.urls'), name='login'),
    path('logout/', include('django.contrib.auth.urls'), name='logout'),
    path('usuario/<int:pk>', views.account, name='account'),
    path('solicitar/<int:jogador>/<int:time_solicitante>/<int:time_solicitado>/<int:pk>', views.solicitar, name='solicitar'),
    path('confirmacao_solicitar/<int:jogador>/<int:time_solicitante>/<int:time_solicitado>/<int:pk>', views.confirmacao_solicitar, name='confirmacao_solicitar'),
    path('aceitar_transferencia/<int:jogador>/<int:pk>/<int:time_solicitante>/<int:notificacao_id>', views.aceitar_transferencia, name='aceitar_transferencia'),
    path('recusar_transferencia/<int:notificacao_id>/<int:pk>', views.recusar_transferencia, name='recusar_transferencia'),
    path('confirmar_dispensar/<int:pk>/<int:admin>', views.confirmar_dispensar, name='confirmar_dispensar'),
    path('dispensar/<int:pk>/<int:admin>', views.dispensar, name='dispensar'),
]