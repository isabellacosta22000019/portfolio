from django.db import models

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    prioridade = models.IntegerField(default=1)
    concluido = models.BooleanField(default=False)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo[:50]



class Post(models.Model):
    autor = models.CharField(max_length=30)
    data = models.DateTimeField(auto_now_add=True)
    titulo = models.CharField(max_length=20)
    description = models.CharField(max_length=280)

    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.titulo[:50]


class PontuacaoQuizz (models.Model):
    nome = models.CharField(max_length=20)
    pontos = models.IntegerField(default=0)

    def __str__(self):
        return self.pontos[:50]