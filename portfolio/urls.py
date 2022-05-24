from django.shortcuts import render
from . import views
from django.urls import path, include

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projectos', views.projectos_page_view, name='projectos'),
    path('edita-cadeira/<int:cadeira_id>', views.edita_cadeira_view, name='editar_cadeira'),
    path('apaga-cadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='apagar_cadeira'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo-post/', views.novo_post_view, name='novo_post'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout')

]
