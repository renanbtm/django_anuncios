from django.db import models


class Categoria(models.Model):
    titulo = models.CharField(max_length=40)

    def __str__(self):
        return self.titulo

    class Meta: # Ordena pelo título
        ordering = ["titulo"]


class AnuncioManager(models.Manager):
    def search(self, value):
        return self.get_queryset().filter(models.Q(titulo__icontains=value) | models.Q(descricao__icontains=value))


class Anuncio(models.Model):
    titulo = models.CharField(max_length=40)
    descricao = models.TextField(null=True, blank=True)
    preco = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to="images/", default="", blank=True, null=True)

    objects = AnuncioManager()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-id"]