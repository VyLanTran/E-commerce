from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile

from .models import Item, Category
from .forms import AddItemForm, EditItemForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def add_item(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)

        if form.is_valid():
            print(form)
            item = form.save(commit=False)
            item.seller = request.user      # to make sure that you are the owner of the item, and only you can update/delete it
            if not item.image:
                default_image_content = 'no images'  
                item.image.save('armchair.jpeg', ContentFile(default_image_content), save=False)
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = AddItemForm()

    return render(request, 'item/add_item.html', {
        'form': form,
        'action': 'add',
    })

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, seller=request.user)  # we have to pass in seller to make sure that only the owner of the product can edit it. If you're logged in as a user but you are not the owner, you can't edit the product

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/add_item.html', {
        'form': form,
         'action': 'edit',
    })

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, seller=request.user)
    item.delete()

    return redirect('my_store:index')