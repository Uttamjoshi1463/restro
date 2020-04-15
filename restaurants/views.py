from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Cart, CartItem
from restaurants.models import Restaurant, Food
from django.contrib.auth.decorators import login_required


# Create your views here.

def view(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        new_total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.food.price) * item.quantity
            new_total += line_total
        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = new_total
        cart.save()
        context = {"cart": cart}
    else:
        empty_message = "Your Cart is Empty, please keep eating!!!!."
        context = {"empty": True, "empty_message":empty_message}
        
    template = "carts/view.html"
    return render(request, template, context)


def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("cart"))

    cartitem = CartItem.objects.get(id=id)
    cartitem.delete()
    # cartitem.cart = None
    # cartitem.save()
    #send "success message"
    return HttpResponseRedirect(reverse("cart"))

# def get_cart_items(request):
#     return CartItem.objects.filter(cart_id=id(request))

# def add_to_cart(request, food_id):
#     request.session.set_expiry(120000)
#     try:
#         the_id = request.session['cart_id']

#     except:
#         new_cart = Cart()
#         new_cart.save()
#         request.session['cart_id'] = new_cart.id
#         the_id = new_cart.id

#     cart = Cart.objects.get(id=the_id)
#     try:
#         food = Food.objects.get(id=food_id)
#     except Food.DoesNotExist:
#         pass
#     except:
#         pass

#     if request.method == "POST":
#         quantity = request.POST['quantity']
#         cart_item = CartItem.objects.create(cart=cart, food=food)
#         if int(quantity) >= 1:
#             cart_item.quantity = quantity
#             cart_item.save()
#             return HttpResponseRedirect(reverse("cart"))

#     #send "error message"
#     return HttpResponseRedirect(reverse("cart"))


def add_to_cart(request, food_id):
    the_id = request.session['cart_id']
    cart = Cart.objects.get(id=the_id)
    foods = Food.objects.get(id=food_id)
    cart_foods = CartItem.objects.create(cart=cart, food=foods)
    if request.method == "POST":
        
        quantity = request.POST['quantity']
        f = get_object_or_404(Food, id=foods)
        # cart_foods = get_cart_items(request)
        food_in_cart = False
        for cart_item in cart_foods:
            if cart_item.food.id == f.id:
                cart_item.augment_quantity(quantity)
                food_in_cart = True
                return HttpResponseRedirect(reverse("cart"))
        if not food_in_cart:
            ci = Cart()
            ci.food = f
            ci.quantity = quantity
            ci.cart_id = id(request)
            ci.save()
            return HttpResponseRedirect(reverse("cart"))