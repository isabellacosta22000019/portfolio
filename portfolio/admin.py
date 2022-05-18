from django.contrib import admin

# Register your models here.
from .models import Tarefa
from .models import Post

admin.site.register(Tarefa)
admin.site.register(Post)
