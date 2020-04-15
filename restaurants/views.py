from django.shortcuts import render, redirect, Http404, HttpResponseRedirect, get_object_or_404
from .models import Restaurant, RestaurantImage, Food
from django.urls import reverse


# Create your views here.

def home(request):
    restaurants = Restaurant.objects.all()
    context = {
        "restaurants":restaurants,
        }
    return render(request, 'home.html', context)

def allrestros(request):
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    template = 'all.html'
    return render(request, template, context)


def singlerestro(request, slug):
    # try:
        restaurant = Restaurant.objects.get(slug=slug)
        foods = Food.objects.filter(restaurant=restaurant)
        images = RestaurantImage.objects.filter(restaurant=restaurant)
        context = {'restaurant': restaurant, 'images': images, 'foods':foods}
        template = 'restaurants/single.html'
        return render(request, template, context)

    # except:
    #     raise Http404

