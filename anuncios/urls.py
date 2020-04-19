from django.urls import path, include

from .views import home
from .views import categoria
from .views import anuncio
from .views import cadastrar_anuncio
from .views import pesquisa

urlpatterns = [
    path('', home, name='home'),
    path('categoria/<int:id>', categoria, name='categoria'),
    path('anuncio/<int:id>', anuncio, name='anuncio'),
    path('cadastro', cadastrar_anuncio, name='cadastrar'),
    path('pesquisa', pesquisa, name="pesquisa"),
    path('', include("django.contrib.auth.urls")),
]