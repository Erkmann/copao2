from datetime import date
from django import forms
from django.db import models


class Time(models.Model):
    logo = models.CharField(max_length = 55)
    nome_time = models.CharField(max_length = 55)
    pontos = models.IntegerField()
    cor = models.CharField(max_length=30)
    saldo_gols = models.IntegerField()
    vitoria = models.IntegerField()

    def __str__(self):
        return self.nome_time

class Partida(models.Model):
    id_time_mandante = models.ForeignKey(Time, on_delete=models.DO_NOTHING, related_name='mandante')
    id_time_visitante = models.ForeignKey(Time, on_delete=models.DO_NOTHING, related_name='visitante')
    data = models.DateField(default=date.today)
    gols_timeA = models.IntegerField(default=0)
    gols_timeB = models.IntegerField(default=0)

    def __str__(self):
        nome = str(self.id_time_mandante) + ' X ' + str(self.id_time_visitante)
        return nome

class Jogador(models.Model):
    numero_camisa = models.IntegerField(default=00)
    nome = models.CharField(max_length=45)
    gols = models.IntegerField(default=0)
    cartao_amarelo = models.IntegerField(default=0)
    cartao_vermelho = models.IntegerField(default=0)
    id_time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=35)

    def __str__(self):
        return self.nome_usuario

class Curtir(models.Model):
    usuario_id_usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    time_id_time = models.ForeignKey(Time, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.usuario_id_usuario) + ' - ' + str(self.time_id_time)