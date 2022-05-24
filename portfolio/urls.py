from django.shortcuts import render
from . import views
from django.urls import path, include

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projectos', views.projectos_page_view, name='projectos'),
    path('edita-post/<int:post_id>', views.edita_post_view, name='editar_post'),
    path('apaga-post/<int:post_id>', views.apaga_post_view, name='apagar_post'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo-post/', views.novo_post_view, name='novo_post'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout')

]
