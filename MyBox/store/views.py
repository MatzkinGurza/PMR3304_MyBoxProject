from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Box
from .forms import BoxForm, BoxFormUpdate
from django.core.paginator import Paginator
from .forms import BoxForm, BoxFormUpdate  # Importa o formulário BoxForm do app store
from .models import Box  # Importa o modelo Box do app store
from django.urls import reverse_lazy, reverse
import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def store_page(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    boxes = Box.objects.filter(seller=seller)

    # Paginação
    paginator = Paginator(boxes, 6)  # 6 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'seller': seller,
        'boxes': page_obj,
    }
    return render(request, 'store/store_page.html', context)


class BoxDetailView(DetailView):
    model = Box
    template_name = 'box_details.html'

    def get_object(self):
        # Use get_object_or_404 to retrieve the Post or raise a 404 if not found
        return get_object_or_404(Box, pk=self.kwargs.get('pk'))
    

class AddBoxView(CreateView):
    model = Box
    form_class = BoxForm
    template_name = 'store/add_box.html'
    # fields = '__all__'
    # fields = ('title', 'tag','body')

    def dispatch(self, request, *args, **kwargs):
        # Redireciona buyers ou usuários não autenticados para uma página informativa
        if not request.user.is_authenticated or not request.user.profile.is_seller:
            return redirect('store:not_seller')
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        # Associa o vendedor à Box
        form.instance.seller = self.request.user

        # Verifica se há uma imagem
        image_file = form.cleaned_data.get('image')  # Substitua 'image' pelo nome do campo no seu form

        if image_file:
            # Enviar a imagem para o Imgur
            url = "https://api.imgur.com/3/image"
            headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
            files = {'image': image_file.read()}

            response = requests.post(url, headers=headers, files=files)
            data = response.json()

            if response.status_code == 200 and data['success']:
                try:
                    if data.get('success'):
                        form.instance.image_url = data['data']['link']  # Salva o link da imagem no campo image_url
                    else:
                        print("Erro no JSON retornado:", data)
                except ValueError:
                    print("Erro ao interpretar JSON:", response.text)                
            else:
                print("Erro no upload do Imgur:", response.text)
        
        return super().form_valid(form)

def not_seller(request):
    return render(request, 'store/not_seller.html')

# class UpdateBoxView(UpdateView):
#     model=Box
#     form_class = BoxFormUpdate
#     template_name= 'store/manage_box.html'
#     success_url = reverse_lazy('home:home')

    # def form_valid(self, form):
        # image_file = form.cleaned_data.get('image')
        # if image_file:
        #     # Enviar a imagem para o Imgur
        #     url = "https://api.imgur.com/3/image"
        #     headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
        #     files = {'image': image_file.read()}

        #     response = requests.post(url, headers=headers, files=files)
        #     data = response.json()

        #     if response.status_code == 200 and data['success']:
        #         form.instance.image_url = data['data']['link']
        #     else:
        #         # Log failure details
        #         print("Imgur upload failed:", response.status_code, data)
            
        #     url = "https://api.imgur.com/3/credits"
        #     headers = {"Authorization": "Client-ID 017429aafa9c2c9"}

        #     response = requests.get(url, headers=headers)
        #     print("Imgur API Quota Check:", response.status_code, response.json())
        
        # return super().form_valid(form)

    
@login_required
def manage_box(request, box_id=None):
    if not request.user.profile.is_seller:
        return HttpResponseForbidden("Apenas vendedores podem gerenciar Boxes.")

    box = None
    if box_id:
        box = get_object_or_404(Box, id=box_id, seller=request.user)

    if request.method == 'POST':
        form = BoxFormUpdate(request.POST, request.FILES, instance=box)
        if form.is_valid():
            box = form.save(commit=False)
            box.seller = request.user

            # Se foi feito upload de uma nova imagem
            if form.cleaned_data['image']:
                image_file = form.cleaned_data['image']
                url = "https://api.imgur.com/3/image"
                headers = {"Authorization": f"Client-ID {settings.IMGUR_CLIENT_ID}"}
                files = {'image': image_file.read()}

                response = requests.post(url, headers=headers, files=files)
                data = response.json()

                if response.status_code == 200 and data['success']:
                    box.image_url = data['data']['link']  # Salva o link da nova imagem da Box
                else:
                    print("Erro no upload do Imgur:", response.text)

            box.save()
            return redirect('store:store_page', seller_id=request.user.id)
    else:
        form = BoxFormUpdate(instance=box)

    return render(request, 'store/manage_box.html', {'form': form, 'box': box})

    
class DeleteBoxView(DeleteView):
    model=Box
    template_name= 'store/delete_box.html'
    success_url = reverse_lazy('home')

    

