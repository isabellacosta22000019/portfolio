# Generated by Django 4.0.4 on 2022-06-12 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_autor_alter_post_description_tfc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tfc',
            name='video',
        ),
    ]
