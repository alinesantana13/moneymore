from django.urls import path
from . import views

urlpatterns = [
    path('pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair")
]