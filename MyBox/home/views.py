from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from store.forms import BoxForm  # Importa o formulário BoxForm do app store
from store.models import Box  # Importa o modelo Box do app store


def home(request):
    # Busca todas as boxes no banco de dados
    boxes = Box.objects.all()
    return render(request, 'home/home.html', {'boxes': boxes})


@login_required
def manage_box(request, box_id=None):
    # Busca a box específica ou inicializa como None
    if box_id:
        box = get_object_or_404(Box, id=box_id, seller=request.user)  # Verifica se o produto pertence ao vendedor
    else:
        box = None

    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES, instance=box)
        if form.is_valid():
            box = form.save(commit=False)
            box.seller = request.user
            box.save()
            return redirect('home')  # Redireciona para a página inicial
    else:
        form = BoxForm(instance=box)

    return render(request, 'home/manage_box.html', {'form': form, 'box': box})
