from django.contrib import admin

from .models import Chamado, Categoria, Equipamentos, Pessoa

# Register your models here.
admin.site.register(Chamado)
admin.site.register(Categoria)
admin.site.register(Equipamentos)
admin.site.register(Pessoa)