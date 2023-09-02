from django.contrib import admin

from .models import ItemConversation, ItemMessage

admin.site.register(ItemConversation)
admin.site.register(ItemMessage)