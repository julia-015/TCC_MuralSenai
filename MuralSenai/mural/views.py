from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .forms import FormAluno
from .models import AAluno




def homepage(request):
    # context = {}
    # context['login_form'] = AuthenticationForm()
    return render(request, 'homepage.html')

def inicio(request):
    return render(request, 'telainicial.html')

def cadastro(request):
    return render(request, 'cadastro.html')

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
            var_curso = form.cleaned_data['curso']
            var_cpf = form.cleaned_data['cpf']
            var_observacoes = form.cleaned_data.get('observacoes', '') 

            try:
                if AAluno.objects.filter(cpf=var_cpf).exists():
                    context.update({"error": "CPF já cadastrado!"})
                else:

                    user_aluno = AAluno (nome=var_nome, curso=var_curso, cpf=var_cpf, observacoes=var_observacoes)
                    user_aluno.save()

                    context.update({"success": "Aluno adicionado com sucesso!"})
            except Exception as e:
                context.update({"error": str(e)})

        else:
            context.update({"form": form})
            return render(request, 'adicionaraluno.html', context)

    else:
        form = FormAluno()
        context.update({"form": form})
        return render(request, 'adicionaraluno.html', context)



def editarcurso(request):
    return render(request, 'editarcurso.html')

def editaraluno(request):
    return render(request, 'editaraluno.html')

