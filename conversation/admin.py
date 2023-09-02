from django.contrib import admin

from .models import ItemConversation, ItemMessage, UserConversation, UserMessage

admin.site.register(UserConversation)
admin.site.register(UserMessage)
admin.site.register(ItemConversation)
admin.site.register(ItemMessage)