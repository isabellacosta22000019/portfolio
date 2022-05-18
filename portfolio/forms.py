from django import forms
from django.forms import ModelForm
from .models import Tarefa
from .models import Post


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'
        # inserção de classes CSS para formatação de cada campo do formulário
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descrição da tarefa...'}),
            'prioridade': forms.NumberInput(attrs={'class': 'form-control', 'max': 3, 'min': 1}),
        }

        # texto a exibir junto à janela de inserção
        labels = {
            'titulo': 'Título',
            'concluido': 'Concluída',
        }

        # texto auxiliar a um determinado campo do formulário
        help_texts = {
            'prioridade': 'prioridade: baixa=1, media=2, alta=3',
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'description': 'Descrição'
        }

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'titulo do post'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'descroção do conteúdo'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nome'}),
        }

        help_texts = {
            'description': 'descrição sobre o Post de até 280 caracteres',
        }


