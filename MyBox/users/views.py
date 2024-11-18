from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial após login
        else:
            messages.error(request, 'Credenciais inválidas')
    return render(request, 'users/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Cadastro realizado com sucesso')
            return redirect('users:login')
    
    return render(request, 'users/register.html')