from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html')

    
def planilha_mensal(request):
    return render(request, 'planilha_mensal.html')

def planilha_anual(request):
    return render(request, 'planilha_anual.html')

def sair(request):
    logout(request)
    return redirect('/auth/login')