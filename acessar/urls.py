from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('planilha_mensal/', views.planilha_mensal, name="planilha_mensal"),
    path('planilha_anual/', views.planilha_anual, name="planilha_anual"),
    path('sair/', views.sair, name="sair")
]