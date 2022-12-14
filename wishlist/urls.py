from django.urls import path
from . import views

app_name = 'wish'

urlpatterns = [
    path('', views.wish_detail, name='wish_detail'),
    path('add/<int:product_id>/', views.wish_add, name='wish_add'),
    path('remove/<int:product_id>/', views.wish_remove, name='wish_remove'),
]