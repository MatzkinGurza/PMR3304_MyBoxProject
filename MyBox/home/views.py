from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.forms import BoxForm, BoxFormUpdate  # Importa o formulário BoxForm do app store
from store.models import Box  # Importa o modelo Box do app store
from users.models import Store  # Importa o modelo Store do app users
from .models import Comment, Rating # Importa o modelo Comment do app home
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, RatingForm
import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
<<<<<<< HEAD
from django.contrib import messages
from django.db.models import Avg

class AddCommentView(CreateView):
    model = Comment
    template_name = 'home/add_comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.box_id = self.kwargs['pk']
        return super().form_valid(form)
=======
from django.db.models import Q
>>>>>>> main

def home(request):
    """
    Renderiza a página inicial com as tags disponíveis para os filtros.
    As boxes são carregadas dinamicamente via API no frontend.
    """
    # Obter todas as categorias únicas para os filtros
    tags = Box.objects.values_list('tag', flat=True).distinct()

    # Garantir que as tags estejam ordenadas para melhor usabilidade
    tags = sorted(tags)

    return render(request, 'home/home.html', {
        'tags': tags,  # Tags disponíveis para o filtro de categorias
    })

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        box = self.get_object()

        # Calculate average rating and count
        ratings = Rating.objects.filter(box=box, status=True)
        context['ratings_count'] = ratings.count()
        average_rating = ratings.aggregate(Avg('rating'))['rating__avg']

        # Handle case where no ratings exist
        context['average_rating'] = average_rating if average_rating is not None else "-"

        # Fetch the user's rating if logged in
        if self.request.user.is_authenticated:
            user_rating = ratings.filter(user=self.request.user).first()
            context['user_rating'] = user_rating.rating if user_rating else None
        else:
            context['user_rating'] = None

        return context

def search_boxes(request):
    query = request.GET.get('q')  # Recupera o termo da barra de pesquisa
    results = Box.objects.filter(name__icontains=query) if query else []  # Filtra as lojas com base na pesquisa
    
    # Adiciona paginação aos resultados
    paginator = Paginator(results, 16)  # Limita 16 lojas por página
    page_number = request.GET.get('page')  # Obtém o número da página da URL
    boxes = paginator.get_page(page_number)  # Obtém a página de lojas correspondente

    return render(request, 'home/search_boxes.html', {'results': results, 'query': query, 'boxes': boxes})

def submit_review(request, box_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = Rating.objects.get(user__id=request.user.id, box__id=box_id)
            form = RatingForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Obrigado! seu rating foi atualizado')
            return redirect(url)
        except Rating.DoesNotExist:
            form = RatingForm(request.POST)
            if form.is_valid():
                data = Rating()
                data.rating = form.cleaned_data['rating']
                data.ip = request.META.get('REMOTE_ADDR')
                data.box_id = box_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Obrigado! seu rating foi enviado')
                return redirect(url)
