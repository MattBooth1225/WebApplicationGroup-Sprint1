from django.contrib import admin
from .models import Product, ProductInstance, Category, ShoppingCart, Payment, Order, WishList, Newsletter
from django.contrib import admin
from .models import Product, ProductInstance, ProductImage, Category, ShoppingCart, Payment, Order, WishList, Newsletter, Contact, Profile


# admin.site.register(Product)
admin.site.register(ProductInstance)
admin.site.register(ProductImage)
# admin.site.register(Categories)
admin.site.register(ShoppingCart)
admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(WishList)
admin.site.register(Newsletter)
admin.site.register(Contact)
admin.site.register(Profile)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
