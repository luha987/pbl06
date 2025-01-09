from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_a, name='item_list_a'),
    path('create/', views.item_create_a, name='item_create_a'),
    path('<int:pk>/edit/', views.item_edit_a, name='item_edit_a'),
    path('<int:pk>/delete/', views.item_delete_a, name='item_delete_a'),
]
