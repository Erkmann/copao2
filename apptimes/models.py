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