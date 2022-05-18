from django.shortcuts import render
from . import views
from django.urls import path, include

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),























    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projectos', views.projectos_page_view, name='projectos'),
    path('nova/', views.nova_tarefa_view, name='nova'),
    path('edita/<int:tarefa_id>', views.edita_tarefa_view, name='edita'),
    path('apaga/<int:tarefa_id>', views.apaga_tarefa_view, name='apaga'),
    path('blog', views.novo_post_view, name='blog'),
    path('quiz', views.quiz_page_view, name='quiz'),

]
