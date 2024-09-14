from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from .forms import ClienteRegistroForm, AdminRegistroForm
from .models import User, Cliente, Administrador

@login_required
def cliente_panel(request):
    return render(request, 'cliente_panel.html')

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

# INDEX PRINCIPAL
def index(request):
    return render(request, 'index.html')

# REGISTRO (CLIENTE - ADMINISTRADOR DISCOTECA)
def registro(request):
    return render(request, 'registro.html')

def cliente_registro(request):
    if request.method == 'POST':
        form = ClienteRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = ClienteRegistroForm()
    return render(request, 'cliente_registro.html', {'form': form})

def administrador_registro(request):
    if request.method == 'POST':
        form = AdminRegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = AdminRegistroForm()
    return render(request, 'admin_registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                
                # Verificamos si es cliente o administrador
                if user.is_admindisco is False and user.is_superuser is False:
                    return redirect('cliente_panel')
                elif user.is_admindisco and user.is_superuser is False:
                    return redirect('admin_panel')
                else:
                    messages.error(request, 'Usted es SuperUsuario')
            else:
                messages.error(request, 'Credenciales incorrectas')
        else:
            messages.error(request, 'Información de login no válida')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# def login_view(request):
#     form = AuthenticationForm(request, data=request.POST or None)

#     if form.is_valid():
#         user = authenticate(
#             username=form.cleaned_data.get('username'),
#             password=form.cleaned_data.get('password')
#         )
#         if user:
#             login(request, user)
#             if user.is_admindisco:
#                 return redirect('admin_panel')
#             if not user.is_superuser:
#                 return redirect('cliente_panel')
#             messages.error(request, 'Usted es SuperUsuario')
#         else:
#             messages.error(request, 'Credenciales incorrectas')
#     elif request.method == 'POST':
#         messages.error(request, 'Información de login no válida')

#     return render(request, 'login.html', {'form': form})