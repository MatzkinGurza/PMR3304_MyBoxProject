from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BoxForm
from .models import Box

def home(request):
    boxes = Box.objects.all()  # Busca todas as boxes no banco de dados
    return render(request, 'home/home.html', {'boxes': boxes})

@login_required
def manage_box(request, box_id=None):
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
            return redirect('home')  # Redireciona para a página inicial ou lista de produtos
    else:
        form = BoxForm(instance=box)

    return render(request, 'home/manage_box.html', {'form': form, 'box': box})
