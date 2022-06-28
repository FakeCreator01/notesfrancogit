# Generated by Django 3.2.6 on 2022-05-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrearNota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('creado', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
        ),
    ]