# Generated by Django 3.0.4 on 2020-04-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0005_anuncio_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]