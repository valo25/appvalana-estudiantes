# Generated by Django 4.0.3 on 2022-04-28 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('valana', '0007_rename_imagen_imagen_foto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Imagen',
            new_name='Foto',
        ),
    ]