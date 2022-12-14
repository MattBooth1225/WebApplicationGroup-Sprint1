from django.urls import path
from store import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('user-profile-shipping-address/', views.user_profile_shipping_address, name='user-profile-shipping-address'),
    path('user-profile-settings/', views.user_profile_settings, name='user-profile-settings'),
    path('user-profile-payment-methods/', views.user_profile_payment_methods, name='user-profile-payment-methods'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('all-products/', views.product_list, name='prod_list'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('search-products', views.search_products, name='search-products'),

    #path('contact-us/', views.contact_us, name='contact-us'),
    #path('user-profile-order-history/', views.user_profile_order_history, name='user-profile-order-history'),
    #path('user-profile-settings/', views.user_profile_settings, name='user_profile_settings'),
    #path('user-profile-shipping-address/', views.user_profile_shipping_address, name='user-profile-shipping-address'),

    # new payment method here
    #path('user-profile-payment-methods/', views.user_profile_payment_methods, name='user-profile-payment-methods'),
    #path('user-profile-order-history/', views.user_profile_order_history, name='user-profile-order-history'),

]
