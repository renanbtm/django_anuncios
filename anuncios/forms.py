from django import forms

from .models import Anuncio


class AnuncioForm(forms.ModelForm):

    class Meta:
        model = Anuncio
        fields = ("titulo", "descricao", "preco", "categoria", "imagem")
        labels = {
            "titulo": "Título",
            "descricao": "Descrição",
            "preco": "Preço",
            "categoria": "Categoria",
            "imagem": "Imagem"
        }