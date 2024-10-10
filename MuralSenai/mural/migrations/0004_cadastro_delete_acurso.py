# Generated by Django 5.1.1 on 2024-10-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mural', '0003_acurso_rename_curso_aaluno_telefone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('profissao', models.CharField(max_length=11, unique=True)),
                ('criarsenha', models.TextField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name='ACurso',
        ),
    ]