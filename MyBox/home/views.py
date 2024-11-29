from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.forms import BoxForm, BoxFormUpdate  # Importa o formulário BoxForm do app store
from store.models import Box  # Importa o modelo Box do app store
from users.models import Store  # Importa o modelo Store do app users
from django.urls import reverse_lazy, reverse
import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

def home(request):
    # Busca todas as boxes no banco de dados
    all_boxes = Box.objects.all()
    paginator = Paginator(all_boxes, 16)  # Limita 16 produtos por página
    page_number = request.GET.get('page')  # Obtém o número da página da URL
    boxes = paginator.get_page(page_number)  # Recupera os objetos da página atual

    return render(request, 'home/home.html', {'boxes': boxes})

def list_stores(request):
    # Busca todas as boxes no banco de dados
    all_stores = Store.objects.all()
    paginators = Paginator(all_stores, 16)  # Limita 16 produtos por página
    page_numbers = request.GET.get('page')  # Obtém o número da página da URL
    stores = paginators.get_page(page_numbers)  # Recupera os objetos da página atual

    return render(request, 'home/list_stores.html', {'stores': stores})

class BoxDetailView(DetailView):
    model = Box
    template_name = 'home/box_details.html'

    def get_object(self):
        # Use get_object_or_404 to retrieve the Post or raise a 404 if not found
        return get_object_or_404(Box, pk=self.kwargs.get('pk'))
    
    # def get_context_data(self, *args, **kwargs):
    #     cat_menu = Category.objects.all()
    #     context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
    #     current_post = get_object_or_404(Post, id=self.kwargs['pk'])
    #     liked = False
    #     if current_post.likes.filter(id=self.request.user.id).exists():
    #         liked=True
    #     context['comments'] = self.object.comments.all().order_by('-date_added')
    #     context['total_likes'] = current_post.total_likes()
    #     context["cat_menu"] = cat_menu
    #     context['liked'] = liked
    #     return context


