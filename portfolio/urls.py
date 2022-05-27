from django.shortcuts import render
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projectos', views.projectos_page_view, name='projectos'),
    path('edita-projecto/<int:projecto_id>', views.edita_projecto_view, name='editar_projecto'),
    path('apaga-projecto/<int:projecto_id>', views.apaga_projecto_view, name='apagar_projecto'),
    path('novo-projecto/', views.novo_projecto_view, name='novo_projecto'),

    path('edita-cadeira/<int:cadeira_id>', views.edita_cadeira_view, name='editar_cadeira'),
    path('apaga-cadeira/<int:cadeira_id>', views.apaga_cadeira_view, name='apagar_cadeira'),
    path('nova-cadeira/', views.nova_cadeira_view, name='novo_cadeira'),
    path('blog', views.blog_page_view, name='blog'),
    path('quiz', views.quiz_page_view, name='quiz'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
