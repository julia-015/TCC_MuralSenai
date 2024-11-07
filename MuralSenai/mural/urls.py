from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('inicio', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro/'),
    path('muralaviso', views.muralaviso, name='muralaviso'),
    path('carometro', views.carometro, name='carometro'),
    path('carometro2', views.carometro2, name='carometro2'),
    path('carometro3', views.carometro3, name='carometro3'),
    path('informacoescar', views.informacoescar, name='informacoescar'),
    path('adicionarcurso', views.adicionarcurso, name='adicionarcurso'),
    path('adicionarturma', views.adicionarturma, name='adicionarturma'),
    path('adicionaraluno', views.adicionaraluno, name='adicionaraluno'),
    path('editarcurso', views.editarcurso, name='editarcurso'),
    path('editaraluno/<int:aluno_id>/', views.editaraluno, name='editaraluno'),
    
]   