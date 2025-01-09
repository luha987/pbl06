from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list_b, name='item_list_b'),
    path('create/', views.item_create_b, name='item_create_b'),
    path('<int:pk>/edit/', views.item_edit_b, name='item_edit_b'),
    path('<int:pk>/delete/', views.item_delete_b, name='item_delete_b'),
]
