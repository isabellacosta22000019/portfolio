from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from matplotlib import pyplot as plt
from .forms import PostForm, CadeiraForm
from .models import *



def home_page_view(request):
    context = {'tarefas': Tarefa.objects.all()}
    return render(request, 'portfolio/home.html', context)


def licenciatura_page_view(request):
    professores = Professor.objects.all()
    cadeiras = Cadeira.objects.all()
    context = {'professores': professores, 'cadeiras': cadeiras}
    return render(request, 'portfolio/licenciatura.html', context)


def projectos_page_view(request):
    return render(request, 'portfolio/projectos.html')

    # Parte do Tutorial Tarefa


def blog_page_view(request):
    form = PostForm
    context = {'posts': Post.objects.all(), 'form': form}
    return render(request, 'portfolio/blog.html', context)


@login_required
def edita_cadeira_view(request, cadeira_id):
    post = Cadeira.objects.get(id=cadeira_id)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form': form, 'cadeira_id': cadeira_id}
    return render(request, 'portfolio/editar_cadeira.html', context)


@login_required
def apaga_cadeira_view(request, cadeira_id):
    Cadeira.objects.get(id=cadeira_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))

    # Fim do Tutorial Tarefa


@login_required
def nova_cadeira_view(request):
    form = CadeiraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:licenciatura'))

    context = {'form_post': form, 'posts': Post.objects.all()}

    return render(request, 'portfolio/licenciatura.html', context)


def quiz_page_view(request):
    p = 0

    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontos=p)
        r.save()
        desenha_grafico_resultados(r)

    context = {'pontos': p}
    return render(request, 'portfolio/quiz.html', context)




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


def desenha_grafico_resultados(request):
    pontuacoes = sorted(PontuacaoQuizz.objects.all(), key=lambda x: x.pontos, reverse=True)

    pessoas_x = []
    pontos_y = []

    for resposta in pontuacoes:
        pessoas_x.append(resposta.nome)
        pontos_y.append(resposta.pontos)

    pessoas_x.reverse()
    pontos_y.reverse()
    plt.barh(pessoas_x, pontos_y)


def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:blog'))
        else:
            return render(request, 'portfolio/blog.html', {
                'message': 'Credenciais Inválidas.'
            })

    return render(request, 'portfolio/login.html')

def view_logout(request):
    logout(request)

    return render(request, 'portfolio/login.html', {
        'message': 'Desconectado.'
    })
