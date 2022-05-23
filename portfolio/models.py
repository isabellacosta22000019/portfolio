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

class Picture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/portfolio/images', blank=True)

    def __str__(self):
        return {self.nome}

class Professor(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return {self.nome}


class Linguagem(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return {self.nome}


class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField
    ano = models.IntegerField()

    def __str__(self):
        return {self.nome}

class Cadeira(models.Model):
    nome = models.CharField(max_length=20)
    ano = models.IntegerField()
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem)
    docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
    docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
    projetos = models.ManyToManyField(Projeto)

    def __str__(self):
        return {self.nome}