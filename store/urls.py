from django.urls import path
from store import views
from django.contrib import admin
from django.urls import path


app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('all-products/', views.AllProductsListView.as_view(), name='all-products'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('all-music/', views.music_list, name='all-music'),
    path('all-merch/', views.merch_list, name='all-merch'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('sale-items/', views.sale_items, name='sales-items'),
    path('user-profile-settings/', views.user_profile_settings, name='user-profile-settings'),
    path('user-profile-shipping-address/', views.user_profile_shipping_address, name='user-profile-shipping-address'),
    path('user-profile-payment-methods/', views.user_profile_payment_methods, name='user-profile-payment-methods'),
    path('user-profile-order-history/', views.user_profile_order_history, name='user-profile-order-history'),
    path('wish-list/', views.wish_list, name='wish-list'),
    #path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
]