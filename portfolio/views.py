from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms

from .models import Tarefa, Post, PontuacaoQuizz
from .forms import TarefaForm, PostForm


def home_page_view(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    return render(request, 'portfolio/licenciatura.html')


def projectos_page_view(request):
    return render(request, 'portfolio/projectos.html')

    # Parte do Tutorial Tarefa


def nova_tarefa_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form}

    return render(request, 'portfolio/nova.html', context)


def edita_tarefa_view(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:home'))

    context = {'form': form, 'tarefa_id': tarefa_id}
    return render(request, 'portfolio/edita.html', context)


def apaga_tarefa_view(request, tarefa_id):
    Tarefa.objects.get(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))

    # Fim do Tutorial Tarefa


def novo_post_view(request):
    context2 = {'post': Post.objects.all()}
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form_post': form, 'post': Post.objects.all()}

    return render(request, 'portfolio/blog.html', context)


def quiz_page_view(request):
    p = 0
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontos=p)
        r.save()

    desenha_grafico_resultados()
    context = {'pontos': p}
    return render(request, 'portfolio/quiz.html', context)


# fazer return render aqui

def pontuacao_quizz(request):
    pontos = 0
    form = request.POST

    if form['p1'] == 'Hyper Text Markup Language':
        pontos += 1

    if form['p2'] == 'Cascading Style Sheets':
        pontos += 1

    if form['p3'] == 'body {color: black;}':
        pontos += 1

    return pontos


def desenha_grafico_resultados():
    pontosLista = PontuacaoQuizz.objecst.all()
    pontosLista.sort(key=lambda x: x.pontos)
    pontosLista.reverse()
    print(pontosLista)

    nomes_x = []
    pontos_y = []

    for pessoa in pontosLista:
        nomes_x.append(pessoa.nome)
        pontos_y.append(pessoa.pontos)

    nomes_x.reverse()
    pontos_y.reverse()

