from django.contrib.auth.models import User
from django.db import models

from item.models import Item

class UserConversation(models.Model):
    members = models.ManyToManyField(User, related_name='direct_conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ('-modified_at',)
    
class UserMessage(models.Model):
    conversation = models.ForeignKey(UserConversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='direct_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class ItemConversation(models.Model):
    item = models.ForeignKey(Item, related_name='conversations', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-modified_at',)
    
class ItemMessage(models.Model):
    conversation = models.ForeignKey(ItemConversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

