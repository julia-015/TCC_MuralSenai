from django import forms

class FormLogin(forms.Form):
    user = forms.CharField(label="Usuário", max_length=20)
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

# class FormCadastro(forms.Form):

