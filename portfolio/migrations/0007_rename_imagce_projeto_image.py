# Generated by Django 4.0.4 on 2022-05-26 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_projeto_imagce_alter_cadeira_docentes_praticas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projeto',
            old_name='imagce',
            new_name='image',
        ),
    ]