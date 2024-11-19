from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Box
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