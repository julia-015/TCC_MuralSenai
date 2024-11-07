from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import FormAluno, FormCadastro, FormLogin, FormCurso, FormTurma
from .models import AAluno, Cadastro, ACurso, ATurma, Login


def homepage(request):
    if request.method == "POST":
        form = FormLogin(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                Login(request, user)
                return redirect('inicio')
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
                if User.objects.filter(email=var_email).exists():
                    context["error"] = "Este email já está cadastrado!"
                else:
                    novo_usuario = User.objects.create_user(
                        username=var_nome,
                        email=var_email,
                        password=var_criar_senha
                    )
                    novo_cadastro = Cadastro(
                        nome=var_nome,
                        email=var_email,
                        profissao=var_profissao,
                        criarsenha=var_criar_senha
                    )
                    novo_cadastro.save()
                    context["success"] = "Cadastro realizado com sucesso!"
                    form = FormCadastro()
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
    else:
        form = FormCadastro()

    context["form"] = form
    return render(request, 'cadastro.html', context)


def muralaviso(request):
    return render(request, 'muralaviso.html')


def carometro(request):
    cursos = ACurso.objects.all()
    context = {'cursos': cursos}
    return render(request, 'carometro.html', context)


def carometro2(request, curso_id):
    turmas = ATurma.objects.filter(curso=curso_id)  # Filtra as turmas pelo curso
    context = {'turmas': turmas}
    return render(request, 'carometro2.html', context)


def carometro3(request, turma_id):
    alunos = AAluno.objects.filter(turma=turma_id)
    context = {'alunos': alunos}
    return render(request, 'carometro3.html', context)


def informacoescar(request):
    alunos = AAluno.objects.all()
    context = {'alunos': alunos}
    return render(request, 'informacoescar.html', context)


def adicionarcurso(request):
    context = {}
    if request.method == "POST":
        form = FormCurso(request.POST)
        if form.is_valid():
            var_curso = form.cleaned_data['curso']
            try:
                if ACurso.objects.filter(curso=var_curso).exists():
                    context["error"] = "Curso já adicionado!"
                else:
                    user_curso = ACurso(curso=var_curso)
                    user_curso.save()
                    context["success"] = "Curso adicionado com sucesso!"
                    form = FormCurso()  
                    return redirect('carometro')
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
        context["form"] = form 
    else:
        form = FormCurso()
    context["form"] = form
    return render(request, 'adicionarcurso.html', context)


def adicionarturma(request):
    context = {}
    if request.method == "POST":
        form = FormTurma(request.POST)
        if form.is_valid():
            var_turma = form.cleaned_data['turma']
            var_periodo = form.cleaned_data['periodo']
            var_curso = form.cleaned_data['curso']

            try:
                if ATurma.objects.filter(turma=var_turma, curso=var_curso).exists():
                    context["error"] = "Essa turma já foi adicionada para o curso selecionado!"
                else:
                    user_turma = ATurma(turma=var_turma, periodo=var_periodo, curso=var_curso)
                    user_turma.save()
                    context["success"] = "Turma adicionada com sucesso!"
                    form = FormTurma()
                    return redirect('carometro2', curso_id=var_curso.id)
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
        context["form"] = form 
    else:
        form = FormTurma()
        context["form"] = form
        return render(request, 'adicionarturma.html', context)

def adicionaraluno(request):
    context = {}
    if request.method == "POST":
        form = FormAluno(request.POST)
        if form.is_valid():
            var_nome = form.cleaned_data['nome']
            var_telefone = form.cleaned_data['telefone']
            var_nome_pai = form.cleaned_data['nome_pai']
            var_nome_mae = form.cleaned_data['nome_mae']
            var_turma = form.cleaned_data['turma']
            var_observacoes = form.cleaned_data.get('observacoes', '')

            try:
                if AAluno.objects.filter(nome=var_nome, turma=var_turma).exists():
                    context["error"] = "Aluno já adicionado na turma!"
                else:
                    user_aluno = AAluno(
                        nome=var_nome,
                        telefone=var_telefone,
                        nome_pai=var_nome_pai,
                        nome_mae=var_nome_mae,
                        observacoes=var_observacoes
                    )
                    user_aluno.save()
                    context["success"] = "Aluno adicionado com sucesso!"
                    form = FormAluno()
                    return redirect('carometro3', turma_id=var_turma.id)
            except Exception as e:
                context["error"] = f"Ocorreu um erro: {str(e)}"
        context["form"] = form
    else:
        form = FormAluno()
        context["form"] = form
        return render(request, 'adicionaraluno.html', context)


def editarcurso(request):
    return render(request, 'editarcurso.html')


def editaraluno(request, aluno_id):
    aluno = get_object_or_404(AAluno, id=aluno_id)
    if request.method == 'POST':
        form = FormAluno(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = FormAluno(instance=aluno)
    return render(request, 'editaraluno.html', {'form': form, 'aluno': aluno})
