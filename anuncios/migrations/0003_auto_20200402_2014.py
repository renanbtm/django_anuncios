# Generated by Django 3.0.4 on 2020-04-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0002_anuncio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anuncio',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['titulo']},
        ),
        migrations.AddField(
            model_name='anuncio',
            name='descricao_mini',
            field=models.TextField(blank=True, null=True),
        ),
    ]
