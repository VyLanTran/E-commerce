from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.view_store, name='view_store'),
]