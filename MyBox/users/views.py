from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from .forms import RegisterForm
from django.urls import reverse_lazy
from MyBox import settings
import requests

def register_view(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        user_type = request.POST.get('user_type')
        # Create a mutable copy of POST data
        post_data = request.POST.copy()

        # Map email dynamically based on user_type
        if user_type == 'buyer':
            print('inside buyer if statement')
            post_data['email'] = post_data.get('buyer_email')  # Map buyer_email to email
            for key in ['store_name', 'cnpj', 'cpf', 'store_email', 'store_phone', 'store_address', 'store_description', 'store_logo_url','store_background_url']:
                post_data[key] = ''  # Clear seller-specific fields
        elif user_type == 'seller':
            print('inside seller elif statement')
            post_data['email'] = post_data.get('store_email')  # Map store_email to email
            for key in ['first_name', 'last_name', 'buyer_cpf', 'buyer_email', 'buyer_phone', 'buyer_address', 'birth_date', 'gender']:
                post_data[key] = ''  # Clear buyer-specific fields

        # Initialize the form with the modified data
        form = RegisterForm(post_data, request.FILES)

        if form.is_valid():
            logo_file = form.cleaned_data.get('logo')
            background_image_file = form.cleaned_data.get('background_image')
            if logo_file:
                url = "https://api.imgur.com/3/image"
                headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
                files = {'image': logo_file.read()}
                response = requests.post(url, headers=headers, files=files)
                data = response.json()
                if response.status_code == 200 and data['success']:
                    form.instance.store_logo_url = data['data']['link']
            if background_image_file:
                url = "https://api.imgur.com/3/image"
                headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
                files = {'image': logo_file.read()}
                response = requests.post(url, headers=headers, files=files)
                data = response.json()
                if response.status_code == 200 and data['success']:
                    form.instance.store_background_url = data['data']['link']
            print('imgur worked')
            profile = form.save(commit=False)
            profile.user_type = user_type  # Explicitly set user_type
            print('saving...')
            profile.save()

            profile.save()
            messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
            return redirect('users:login')
        else:
            print("Form errors:", form.errors)  # Debug: Print form errors
            messages.error(request, 'Houve um problema com o cadastro. Verifique os dados e tente novamente.')
    else:
        form = RegisterForm()


    return render(request, 'users/register.html', {'form': form})



def save(self, commit=True):
    user = User.objects.create_user(
        username=self.cleaned_data['username'],
        email=self.cleaned_data['email'],
        password=self.cleaned_data['password']
    )

    # Avoid creating multiple profiles for the same user
    if Profile.objects.filter(user=user).exists():
        raise ValueError("A Profile for this user already exists.")

    profile = super().save(commit=False)
    profile.user = user

    # Upload images to Imgur and save URLs
    if 'logo' in self.files:
        profile.store_logo_url = self.upload_to_imgur(self.files['logo'])
    if 'background_image' in self.files:
        profile.store_background_url = self.upload_to_imgur(self.files['background_image'])

    if commit:
        user.save()
        profile.save()
    return profile

# def register_view(request):
#     if request.method == 'POST':
#         print(request.POST)  # Debug: Log the submitted data
#         form = RegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             profile.user_type = request.POST.get('user_type')  # Debug: Check user_type
#             print(f"User Type: {profile.user_type}")  # Debug: Print user_type
#             profile.save()
#             messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
#             return redirect('users:login')
#         else:
#             print(form.errors)  # Debug: Print form errors
#             messages.error(request, 'Houve um problema com o cadastro. Verifique os dados e tente novamente.')
#     else:
#         form = RegisterForm()
        
#     return render(request, 'users/register.html', {'form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Cadastro realizado com sucesso! Faça login para continuar.')
#             return redirect('users:login')
#         else:
#             messages.error(request, 'Houve um problema com o cadastro. Verifique os dados e tente novamente.')
#     else:
#         form = RegisterForm()

#     return render(request, 'users/register.html', {'form': form})

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