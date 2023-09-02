from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('item_conversation/<int:pk>/', views.item_conversation_detail, name='item_conversation_detail'),
    path('new_item_conversation/<int:item_id>/', views.new_item_conversation, name='new_item_conversation'),
]