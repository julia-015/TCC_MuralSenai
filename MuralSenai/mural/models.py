from django.db import models
from django.contrib.auth.hashers import make_password


class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100, default='default_password')

    def __str__(self):
        return self.username


class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    criarsenha = models.TextField(max_length=1000)

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)

    def __str__(self):
        return self.nome


class AAluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    nome_pai = models.CharField(max_length=100, default='Nao informado')
    nome_mae = models.CharField(max_length=100, default='Nao informado')
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

