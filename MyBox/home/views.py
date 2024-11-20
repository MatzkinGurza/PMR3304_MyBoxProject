from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.forms import BoxForm, BoxFormUpdate  # Importa o formulário BoxForm do app store
from store.models import Box  # Importa o modelo Box do app store
from django.urls import reverse_lazy, reverse
import requests
from django.conf import settings
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def home(request):
    # Busca todas as boxes no banco de dados
    boxes = Box.objects.all()
    return render(request, 'home/home.html', {'boxes': boxes})


