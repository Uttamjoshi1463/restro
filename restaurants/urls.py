from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('restaurants/<slug>/', views.singlerestro, name='single_restaurant'),
    path('restaurants/', views.allrestros, name="restaurants"),

] 