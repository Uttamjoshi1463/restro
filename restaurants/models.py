from django.db import models
from django.urls import reverse


# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pan_number = models.CharField(max_length=50)
    email = models.EmailField()
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'slug')

    def get_absolute_url(self):
        return reverse("single_restaurant", kwargs={"slug":self.slug})

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='restaurants/images/')



class Contact(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False, blank=False)
    phone_num = models.CharField(max_length=15, null=True, blank=False)




class Food(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False, blank=False)
    image = models.ImageField(upload_to='foods/images/')
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)



    def __str__(self):
        return str(self.name) + "@" + self.restaurant.name

