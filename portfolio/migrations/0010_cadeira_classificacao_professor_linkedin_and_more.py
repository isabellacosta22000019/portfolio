# Generated by Django 4.0.4 on 2022-05-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_alter_projeto_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadeira',
            name='classificacao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='linkedin',
            field=models.URLField(default='https://www.linkedin.com/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projeto',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
