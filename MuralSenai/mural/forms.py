from django import forms
from .models import AAluno


class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

class FormAluno(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Nome', 'class': 'form-control'})
    )
    curso = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Cursos', 'class': 'form-control'})
    )
    cpf = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': 'CPF', 'class': 'form-control'})
    )
    observaçoes = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={'placeholder': 'Observações', 'class': 'form-control'})
    )

