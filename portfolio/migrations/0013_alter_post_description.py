# Generated by Django 4.0.4 on 2022-05-29 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_professor_p_remove_cadeira_docentes_praticas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=280),
        ),
    ]
