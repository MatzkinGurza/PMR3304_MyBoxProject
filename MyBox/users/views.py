from django.shortcuts import render, redirect,  get_object_or_404
from django.views import generic, View
from .forms import UserProfileForm, StoreForm
from django.contrib import messages
from MyBox import settings
import requests
from django.contrib.auth.models import User
from .models import Profile, Store, Cart, CartItem
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserProfileForm, StoreForm, EditUserForm
from django.contrib.auth.views import PasswordChangeView
import requests
from django.conf import settings
from store.models import Box
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateStoreView(CreateView):
    model = Profile
    form_class = StoreForm
    template_name = 'users/create_store.html'
    #fields = '__all__'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        logo_file = form.cleaned_data.get('logo')
        bg_file = form.cleaned_data.get('background')
        if logo_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': logo_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                try:
                    data = response.json()
                    if data.get('success'):
                        form.instance.logo_url = data['data']['link']
                    else:
                        print("Erro no JSON retornado:", data)
                except ValueError:
                    print("Erro ao interpretar JSON:", response.text)                
            else:
                print("Erro no upload do Imgur:", response.text)

        if bg_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': bg_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                    try:
                        data = response.json()
                        if data.get('success'):
                            form.instance.background_url = data['data']['link']
                        else:
                            print("Erro no JSON retornado:", data)
                    except ValueError:
                        print("Erro ao interpretar JSON:", response.text)
            else:
                print("Erro no upload do Imgur:", response.text)
                
        return super().form_valid(form)


class CreateProfileView(CreateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'users/create_profile.html'
    #fields = '__all__'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # Check if the user already has a profile
        if Profile.objects.filter(user=self.request.user).exists():
            messages.error(self.request, "You already have a profile.")
            return redirect('home:home')  # Redirect to a safe place
        # Assign the logged-in user to the profile
        form.instance.user = self.request.user
        return super().form_valid(form)
            
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'users/user_profile.html'

    # def get_context_data(self, *args, **kwargs):
    #     users = Profile.objects.all()
    #     context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
    #     page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
    #     context["page_user"] = page_user
    #     user_boxs = Box.objects.filter(author=page_user.user)
    #     context["user_boxs"] = user_boxs
    #     return context
    

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "users/register.html"
    success_url = reverse_lazy('users:login')

class UserEditView(generic.UpdateView):
    form_class = EditUserForm
    template_name = "users/edit_profile.html"
    success_url = reverse_lazy('home:home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    forms_classe = PasswordChangeForm
    success_url = reverse_lazy('home:home')

class AddToCartView(LoginRequiredMixin, View):
    """Adiciona um pacote ao carrinho do usuário."""

    def post(self, request, *args, **kwargs):
        box_id = kwargs.get('box_id')  # ID do pacote recebido pela URL
        quantity = int(request.POST.get('quantity', 1))  # Quantidade passada no formulário ou padrão 1

        # Busca o pacote pelo ID ou retorna 404
        box = get_object_or_404(Box, id=box_id)

        # Busca ou cria o carrinho do usuário
        cart, _ = Cart.objects.get_or_create(buyer=request.user)

        # Busca ou cria o item no carrinho
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, box=box)

        if not item_created:
            # Incrementa a quantidade se o item já existir no carrinho
            cart_item.quantity += quantity
        else:
            # Define a quantidade para o novo item
            cart_item.quantity = quantity

        cart_item.save()

        # Envia mensagem de sucesso
        messages.success(request, f"'{box.name}' foi adicionado ao seu carrinho!")

        # Redireciona para a página do carrinho
        return redirect(reverse('users:detail'))
    
class CartDetailView(LoginRequiredMixin, TemplateView):
    template_name = "users/cart_detail.html"  # Nome do template para renderização

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Obtém o carrinho do usuário logado
        cart = Cart.objects.filter(buyer=self.request.user).first()

        # Adiciona o carrinho e os itens ao contexto
        context['cart'] = cart
        context['cart_items'] = cart.cart_items.all() if cart else []
        context['total_price'] = cart.total_price if cart else 0

        return context
    


# def login_view(request):
#     if request.method == 'POST':
#         identifier = request.POST['username']  # Pode ser username ou email
#         password = request.POST['password']

#         # Tentar autenticar pelo username
#         user = authenticate(request, username=identifier, password=password)
        
#         # Se falhar, verificar se é email
#         if user is None:
#             try:
#                 user_obj = User.objects.get(email=identifier)
#                 user = authenticate(request, username=user_obj.username, password=password)
#             except User.DoesNotExist:
#                 user = None

#         if user is not None:
#             if user.is_active:  # Verifica se o usuário está ativo
#                 login(request, user)

#                 # Redirecionamento baseado no tipo de usuário
#                 profile = Profile.objects.filter(user=user).first()
#                 if profile:
#                     if profile.is_seller:
#                         return redirect('store:store_page', seller_id=user.id)  # Página da loja
#                     elif profile.is_buyer:
#                         return redirect('home:home')  # Página inicial para compradores
#                 else:
#                     messages.error(request, 'Seu perfil não está configurado corretamente.')
#                     return redirect('users:login')

#             else:
#                 messages.error(request, 'Sua conta está inativa.')
#         else:
#             messages.error(request, 'Credenciais inválidas. Verifique o nome de usuário ou email e senha.')

#     return render(request, 'users/login.html')

def logout_view(request):
    if request.method == 'POST':  # Confirmação do logout
        logout(request)
        return redirect('home:home')  # Redirecionar após o logout
    return render(request, 'users/logout.html')  # Página de confirmação