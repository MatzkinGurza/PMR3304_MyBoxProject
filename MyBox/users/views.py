from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST['username']  # Pode ser username ou email
        password = request.POST['password']

        # Tentar autenticar pelo username
        user = authenticate(request, username=identifier, password=password)
        
        # Se falhar, verificar se é email
        if user is None:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        # Validação extra: Verificar se o usuário é ativo
        if user is not None:
            if user.is_active:  # Verifica se o usuário está ativo
                login(request, user)

                # Redirecionamento personalizado com base no tipo de usuário
                try:
                    profile = user.profile  # Assume que há um modelo de Profile relacionado ao User
                    if profile.user_type == "seller":
                        return redirect('store:store_page', seller_id=user.id)  # Página da loja
                    else:  # Default para cliente
                        return redirect('home')
                except AttributeError:
                    # Caso o perfil não esteja configurado corretamente
                    messages.error(request, 'Erro ao identificar o tipo de usuário.')
                    return redirect('home')
            else:
                messages.error(request, 'Sua conta está inativa.')
        else:
            messages.error(request, 'Credenciais inválidas.')

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