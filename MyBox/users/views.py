from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('users:login')
        else:
            messages.error(request, 'Houve um problema com o cadastro. Verifique os dados e tente novamente.')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

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

        if user is not None:
            if user.is_active:  # Verifica se o usuário está ativo
                login(request, user)

                # Redirecionamento baseado no tipo de usuário
                profile = Profile.objects.filter(user=user).first()
                if profile:
                    if profile.is_seller:
                        return redirect('store:store_page', seller_id=user.id)  # Página da loja
                    elif profile.is_buyer:
                        return redirect('home:home')  # Página inicial para compradores
                else:
                    messages.error(request, 'Seu perfil não está configurado corretamente.')
                    return redirect('users:login')

            else:
                messages.error(request, 'Sua conta está inativa.')
        else:
            messages.error(request, 'Credenciais inválidas. Verifique o nome de usuário ou email e senha.')

    return render(request, 'users/login.html')

# def register_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
        
#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Nome de usuário já existe.')
#         elif User.objects.filter(email=email).exists():
#             messages.error(request, 'Este email já está em uso.')
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             # Criar um perfil padrão para o novo usuário
#             Profile.objects.create(user=user)
#             messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
#             return redirect('users:login')
    
#     return render(request, 'users/register.html')

def logout_view(request):
    if request.method == 'POST':  # Confirmação do logout
        logout(request)
        return redirect('home:home')  # Redirecionar após o logout
    return render(request, 'users/logout.html')  # Página de confirmação