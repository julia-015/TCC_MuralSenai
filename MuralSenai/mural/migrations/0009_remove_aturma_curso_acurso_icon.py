# Generated by Django 5.1.1 on 2024-10-29 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mural', '0008_aturma_curso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aturma',
            name='curso',
        ),
        migrations.AddField(
            model_name='acurso',
            name='icon',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
