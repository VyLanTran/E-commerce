from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('new_user_conversation/<int:receiver_id>/', views.new_user_conversation, name='new_user_conversation'),
    path('new_item_conversation/<int:item_id>/', views.new_item_conversation, name='new_item_conversation'),
    path('user_conversation/<int:pk>/', views.user_conversation_detail, name='user_conversation_detail'),
    path('item_conversation/<int:pk>/', views.item_conversation_detail, name='item_conversation_detail'),
]