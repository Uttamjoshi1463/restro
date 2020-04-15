from django.contrib import admin
from .models import Restaurant, Contact, RestaurantImage, Food

# Register your models here.

class ContactInline(admin.StackedInline):
    model = Contact
    extra = 1

class RestaurantImageInline(admin.StackedInline):
    model = RestaurantImage
    extra = 1

class FoodInline(admin.StackedInline):
    model = Food
    extra = 1



class RestaurantAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    list_display = ('name', 'pan_number', 'email')
    list_filter = ('name', 'updated')
    search_fields = ('name',)
    readonly_fields = ['updated', 'timestamp']
    list_editable = ['pan_number', 'email']
    prepopulated_fields = {"slug": ("name",)}
    class Meta:
        model = Restaurant

    inlines = [ContactInline, RestaurantImageInline, FoodInline]



admin.site.site_header = 'Restro Admin Dashboard'
admin.site.register(Restaurant, RestaurantAdmin)
# admin.site.register(Contact)
# admin.site.register(RestaurantImage)
admin.site.register(Food)

