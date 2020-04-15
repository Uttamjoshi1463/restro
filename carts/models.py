from django.db import models
from django.urls import reverse
from restaurants.models import Restaurant, Food
from django.contrib.auth.models import User



# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, default=0)
    quantity = models.IntegerField(default=0)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id)
        except:
            return self.food.name

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.food.name

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)


    # def __unicode__(self):
    #     return "Cart id: %s" %(self.id)


    def __str__(self):
        return "Cart id: %s" %(self.id)
