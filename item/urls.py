from django.urls import path

from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('add_item/', views.add_item, name='add_item'),
    path('<int:pk>/edit_item/', views.edit_item, name='edit_item'),
    path('<int:pk>/delete_item/', views.delete_item, name='delete_item'),
]