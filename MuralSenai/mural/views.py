from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import FormAluno, FormCadastro, FormLogin
from .models import AAluno, Cadastro




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormLogin

def homepage(request):
    if request.method == "POST":
        form = FormLogin(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redireciona para a página desejada
            else:
                form.add_error(None, "Nome de usuário ou senha inválidos.")
    else:
        form = FormLogin()

    return render(request, 'homepage.html', {'form': form})


def inicio(request):
    return render(request, 'telainicial.html')

def cadastro(request):
    context = {}

    if request.method == "POST":
        form = FormCadastro(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_email = form.cleaned_data['email']
            var_profissao = form.cleaned_data['profissao']
            var_criar_senha = form.cleaned_data['criarsenha']

            try:
                if Cadastro.objects.filter(profissao=var_profissao).exists():
                    context["error"] = "Esta profissão já está cadastrada!"
                else:
                    novo_cadastro = Cadastro(
                        nome=var_nome,
                        email=var_email,
                        profissao=var_profissao,
                        criarsenha=var_criar_senha,
                    )
                    novo_cadastro.set_senha(var_criar_senha)  # Salva a senha de forma segura
                    novo_cadastro.save()

                    context["success"] = "Cadastro realizado com sucesso!"
                    form = FormCadastro()  # Resetar o formulário após o sucesso
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
        else:
            context["form"] = form
    else:
        form = FormCadastro()

    context["form"] = form
    return render(request, 'cadastro.html', context)

    return render(request, 'cadastro.html', {'form': form})
    

def muralaviso(request):
    return render(request, 'muralaviso.html')

def carometro(request):
    return render(request, 'carometro.html')

def carometro2(request):
    return render(request, 'carometro2.html')

def carometro3(request):
    return render(request, 'carometro3.html')

def informaçoescar(request):
    return render(request, 'informaçoescar.html')

def adicionarcurso(request):
    return render(request, 'adicionarcurso.html')
    
def adicionaraluno(request):
    context = {}

    if request.method == "POST":
        form = FormAluno(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_telefone = form.cleaned_data['telefone']
            var_nome_pai = form.cleaned_data['nome_pai']
            var_nome_mae = form.cleaned_data['nome_mae']
            var_observacoes = form.cleaned_data.get('observacoes', '')

            try:
                if AAluno.objects.filter(nome=var_nome).exists():
                    context["error"] = "Nome já cadastrado!"
                else:
                    user_aluno = AAluno(
                        nome=var_nome,
                        telefone=var_telefone,
                        nome_pai=var_nome_pai,  # Corrigido para nome_pai
                        nome_mae=var_nome_mae,  # Corrigido para nome_mae
                        observacoes=var_observacoes
                    )
                    user_aluno.save()

                    context["success"] = "Aluno adicionado com sucesso!"
                    form = FormAluno()  # Resetar o formulário após o sucesso
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
        else:
            context["form"] = form
    else:
        form = FormAluno()

    context["form"] = form
    return render(request, 'adicionaraluno.html', context)


def editarcurso(request):
    return render(request, 'editarcurso.html')

def editaraluno(request):
    return render(request, 'editaraluno.html')

