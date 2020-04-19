from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Categoria
from .models import Anuncio
from .forms import AnuncioForm


def home(request):
    categorias = Categoria.objects.all()
    ultimos_anuncios = Anuncio.objects.all()[:12]
    return render(request, "home.html", {"categorias": categorias, "anuncios": ultimos_anuncios})


def categoria(request, id): #Tem que ter o mesmo nome que tá na view <int:id>
    categorias = Categoria.objects.all()
    cat = get_object_or_404(Categoria, id=id)
    anuncios = Anuncio.objects.filter(categoria=cat)
    return render(request, "home.html", {"categorias": categorias, "anuncios": anuncios, "cat": cat})


def anuncio(request, id):
    anuncio = get_object_or_404(Anuncio, id=id)
    categorias = Categoria.objects.all()
    return render(request, "anuncio.html", {"categorias": categorias, "anuncio": anuncio})


def cadastrar_anuncio(request):
    if request.method == "POST":
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            novo_anuncio = form.save()
            return redirect("anuncio", id=novo_anuncio.id)
    else:
        form = AnuncioForm()
    categorias = Categoria.objects.all()
    return render(request, "cadastro.html", {"categorias": categorias, "form": form})


def pesquisa(request):
    valor = request.GET.get("campoPesquisa", "")
    anuncios = Anuncio.objects.search(valor)
    categorias = Categoria.objects.all()
    return render(request, "pesquisa.html", {"anuncios": anuncios, "categorias": categorias, "valor": valor})