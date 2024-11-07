# Generated by Django 5.1.1 on 2024-11-07 12:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mural', '0010_aturma_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField(verbose_name='Mensagem de Aviso')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='aaluno',
            name='turma',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mural.aturma'),
        ),
    ]