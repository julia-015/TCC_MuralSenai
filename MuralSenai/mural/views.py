from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm



def homepage(request):
    # context = {}
    # context['login_form'] = AuthenticationForm()
    return render(request, 'homepage.html')

def inicio(request):
    return render(request, 'telainicial.html')

