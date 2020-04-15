from django.urls import path
from .import views


urlpatterns = [
    path('cart/', views.view, name="cart"),
    path('cart/remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    # path('cart/add/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
] 