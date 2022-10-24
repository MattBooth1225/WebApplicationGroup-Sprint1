from django.urls import path
from store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-products/', views.AllProductsListView.as_view(), name='all-products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('all-music/', views.music_list, name='all-music'),
    path('all-merch/', views.merch_list, name='all-merch'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('sale-items/', views.sale_items, name='sales-items'),
    path('user-profile-settings/', views.user_profile_settings, name='user-profile-settings'),
    path('wish-list/', views.wish_list, name='wish-list')
]