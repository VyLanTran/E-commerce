from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from item.models import Item, User
from .forms import ItemMessageForm, UserMessageForm
from .models import ItemConversation, UserConversation

@login_required
def new_user_conversation(request, receiver_id):
    receiver = get_object_or_404(User, pk=receiver_id)
    
    user_conversations = UserConversation.objects.filter(
        Q(members=request.user) & Q(members=receiver)
    )

    if user_conversations:
        return redirect('conversation:user_conversation_detail', pk=user_conversations.first().id)

    if request.method == 'POST':
        form = UserMessageForm(request.POST)

        if form.is_valid():
            user_conversation = UserConversation.objects.create()
            user_conversation.members.add(request.user)
            user_conversation.members.add(receiver)
            user_conversation.save()

            user_message = form.save(commit=False)
            user_message.conversation = user_conversation
            user_message.sender = request.user
            user_message.save()

            return redirect('conversation:inbox')
    else:
        form = UserMessageForm()
    
    return render(request, 'conversation/new_conversation.html', {
        'form': form
    })

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
    user_conversations = UserConversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'item_conversations': item_conversations,
        'user_conversations': user_conversations
    })

@login_required
def user_conversation_detail(request, pk):
    user_conversation = UserConversation.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = UserMessageForm(request.POST)

        if form.is_valid():
            user_message = form.save(commit=False)
            user_message.conversation = user_conversation
            user_message.sender = request.user
            user_message.save()

            user_conversation.save()

            return redirect('conversation:user_conversation_detail', pk=pk)
    else:
        form = UserMessageForm()

    return render(request, 'conversation/user_conversation_detail.html', {
        'user_conversation': user_conversation,
        'form': form
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

    return render(request, 'conversation/item_conversation_detail.html', {
        'item_conversation': item_conversation,
        'form': form
    })