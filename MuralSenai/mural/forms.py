from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AAluno, Cadastro, ACurso, Login, ATurma


class FormLogin(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class FormCadastro(forms.Form):
        nome = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        profissao = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        criarsenha = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))


class FormAluno(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefone = forms.CharField(
        max_length=15,  # Limite adequado para um número de telefone
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_pai = forms.CharField(  # Certifique-se de usar o nome correto (nome_pai)
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_mae = forms.CharField(  # Certifique-se de usar o nome correto (nome_mae)
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    observacoes = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control'})  # Use Textarea para observações mais longas
    )

class FormCurso(forms.Form):
    curso = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

class FormTurma(forms.Form):
    turma = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    periodo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))