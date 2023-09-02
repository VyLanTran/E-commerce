from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from item.models import Item 

@login_required
def index(request):
    items = Item.objects.filter(seller=request.user)

    return render(request, 'store/index.html', {
        'items': items,
        'seller': request.user,
    })

@login_required
def view_store(request, pk):
    user = get_object_or_404(User, pk=pk)
    items = Item.objects.filter(seller=user)

    return render(request, 'store/index.html', {
        'items': items,
        'seller': user,
    })