from django.db import models


class Login(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500)
    logo = models.ImageField(upload_to="logo/")

    def __str__(self):
        return self.titulo


class AAluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
