# Generated by Django 4.0.3 on 2022-04-30 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valana', '0008_rename_imagen_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='posteo',
            name='autor',
            field=models.CharField(default='anonimo', max_length=20),
        ),
        migrations.AddField(
            model_name='posteo',
            name='imagenposteo',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesposteos'),
        ),
        migrations.AddField(
            model_name='posteo',
            name='subtitulo',
            field=models.CharField(default='-', max_length=150),
        ),
    ]
