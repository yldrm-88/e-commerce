from django.contrib import admin
from .models import*
# Register your models here.

class CoffeeModels(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_per_page=10
    list_display_links=['id','name']
    list_filter=['category']

admin.site.register(Product,CoffeeModels)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingOrder)
admin.site.register(Category)