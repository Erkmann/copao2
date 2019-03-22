from django.contrib import admin
from apptimes.models import *
# Register your models here.
admin.site.register(Time)
admin.site.register(Jogador)
admin.site.register(Curtir)
admin.site.register(Partida)
admin.site.register(Usuario)
admin.site.register(Transferencia)
admin.site.register(TransferenciaJogador)

