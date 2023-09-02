from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from item.models import Item

from .forms import ItemMessageForm
from .models import ItemConversation

@login_required
def new_item_conversation(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    item_conversations = ItemConversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if item_conversations:
        return redirect('conversation:item_conversation_detail', pk=item_conversations.first().id)

    if request.method == 'POST':
        form = ItemMessageForm(request.POST)

        if form.is_valid():
            item_conversation = ItemConversation.objects.create(item=item)
            item_conversation.members.add(request.user)
            item_conversation.members.add(item.seller)
            item_conversation.save()

            item_message = form.save(commit=False)
            item_message.conversation = item_conversation
            item_message.sender = request.user
            item_message.save()

            return redirect('conversation:inbox')
    else:
        form = ItemMessageForm()
    
    return render(request, 'conversation/new_conversation.html', {
        'form': form
    })

@login_required
def inbox(request):
    item_conversations = ItemConversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'item_conversations': item_conversations
    })

@login_required
def item_conversation_detail(request, pk):
    item_conversation = ItemConversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ItemMessageForm(request.POST)

        if form.is_valid():
            item_message = form.save(commit=False)
            item_message.conversation = item_conversation
            item_message.sender = request.user
            item_message.save()

            item_conversation.save()

            return redirect('conversation:item_conversation_detail', pk=pk)
    else:
        form = ItemMessageForm()

    return render(request, 'conversation/conversation_detail.html', {
        'item_conversation': item_conversation,
        'form': form
    })