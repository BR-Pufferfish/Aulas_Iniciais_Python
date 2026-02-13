from django.contrib import admin

from .models import Chamado, Categoria, Equipamento, Pessoa

# Register your models here.
admin.site.register(Chamado)
admin.site.register(Categoria)
admin.site.register(Equipamento)
admin.site.register(Pessoa)