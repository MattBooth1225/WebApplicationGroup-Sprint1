from django.contrib import admin
from .models import Product, ProductInstance, Categories, ShoppingCart

admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(Categories)
admin.site.register(ShoppingCart)
