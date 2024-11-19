from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Box
from .forms import BoxForm
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    return render(request, 'store/dashboard.html')

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

@login_required
def manage_box(request, box_id=None):
    if box_id:
        box = get_object_or_404(Box, id=box_id, seller=request.user)  # Verifica se o Box pertence ao vendedor
    else:
        box = None

    if request.method == 'POST':
        form = BoxForm(request.POST, request.FILES, instance=box)
        if form.is_valid():
            box = form.save(commit=False)
            box.seller = request.user
            box.save()
            return redirect('store:store_page', seller_id=request.user.id)  # Redireciona para a página da loja
    else:
        form = BoxForm(instance=box)

    return render(request, 'store/manage_box.html', {'form': form, 'box': box})