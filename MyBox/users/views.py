from django.shortcuts import render, redirect,  get_object_or_404
from django.views import generic, View
from .forms import UserProfileForm, StoreForm
from django.contrib import messages
from MyBox import settings
import requests
from django.contrib.auth.models import User
from .models import Profile, Store, Cart, CartItem, Subscription, Payment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView, DeleteView, ListView
from django.urls import reverse_lazy
from .forms import SignUpForm, UserProfileForm, StoreForm, EditUserForm, PaymentForm
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
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity

        cart_item.save()

        return redirect(reverse('users:cart'))
    
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
        context['form'] = PaymentForm()

        return context
    
class DeleteCartItem(DeleteView):
    model=CartItem
    template_name = 'users/cart_detail.html'
    success_url = reverse_lazy('users:cart')

class CreateSubscriptionView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Trata os dados enviados pelo usuário
        payment_id = kwargs.get('payment_id')
        print(payment_id)
        payment = Payment.objects.get(id=payment_id)
        subscription_id = kwargs.get('pk')
        subscription = Subscription.objects.create(
            payment = payment,
            user = request.user,
            is_active=True    
        )
        subscription.save()   
        return redirect('users:subscriptions')
    
class CancelSubscriptionView(View):
    def post(self, request, *args, **kwargs):
        subscription_id = kwargs.get('pk')
        subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)

        if subscription.is_active:
            subscription.is_active = False
            subscription.save()
            messages.success(request, "Subscrição cancelada com sucesso!")
        else:
            messages.warning(request, "Esta subscrição já está cancelada.")

        return redirect('users:subscription')
    
class SubscriptionListView(LoginRequiredMixin, ListView):
    model = Subscription
    subscription = Subscription.objects.all()
    template_name = 'users/subscription.html'  # O template que será usado para exibir as subscrições
    context_object_name = 'subscriptions'  # Nome do contexto que será passado para o template
    paginate_by = 10  # Paginação
    payment = Subscription.payment

    def get_queryset(self):
        """Retorna todas as subscrições do usuário logado"""
        return Subscription.objects.filter(user=self.request.user)

    
class CreatePaymentView(View):
    def get(self, request, *args, **kwargs):
        selected_box_id = request.GET.get('selected_box')
        form = PaymentForm()  
         # Se não houver selected_box, exibe uma mensagem de erro
        if not selected_box_id:
            error = "Por favor, volte e selecione uma box."
            return render(request, 'users/payment.html', {'form': form, 'error': error})
        
        # Passa o selected_box_id para o contexto
        print(f"selected:{selected_box_id}")
        return render(request, 'users/payment.html', {'form': form, 'selected_box_id': selected_box_id})


    def post(self, request, *args, **kwargs):
        selected_box_id = request.POST.get('selected_box')
        form = PaymentForm(request.POST) 
        if not selected_box_id:
            error = "Por favor, volte e selecione uma box."
            return render(request, 'users/payment.html', {'form': form, 'error': error})
        
        # Se o formulário for válido
        if form.is_valid():
            payment = form.save(commit=False)
            payment_id = kwargs.get('pk')
            payment.box_id = selected_box_id # Associa a Box selecionada
            payment.save()  # Salva o pagamento no banco de dados
            return render(request, 'users/payment_confirmation.html', {'payment': payment, 'form': form})

        # Caso o formulário não seja válido, renderiza novamente com os erros
        return render(request, 'users/payment.html', {'form': form, 'error': 'Formulário inválido.'})


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