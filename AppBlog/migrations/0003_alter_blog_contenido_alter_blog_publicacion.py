# Generated by Django 4.1.3 on 2022-12-04 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_autores_categoria_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='publicacion',
            field=models.DateField(),
        ),
    ]
