
"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, listar, criar, fechar, novoChamado, baseHtml # Importamos a função que criamos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),  # Deixando vazio '', a página aparece na raiz do site
    path('listar', listar), # Página inicial lista os chamados
    path('novo/<str:lab>/<str:problema>/<str:prioridade>/', criar), # Rota dinâmica
    path('fechar/<int:indice>', fechar), # Rota dinâmica
    path('exibirNovoChamado', novoChamado),
    path('base', baseHtml),
]
