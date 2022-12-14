from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from .wishlist import Wishlist
from .forms import WishAddProductForm


@require_POST
def wish_add(request, product_id):
    wish = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wish.add(product=product)
    return redirect('wish:wish_detail')


#@require_POST
def wish_remove(request, product_id):
    wish = Wishlist(request)
    product = get_object_or_404(Product, id=product_id)
    wish.remove(product)
    wish.save()
    return redirect('wish:wish_detail')


def wish_detail(request):
    wish = Wishlist(request)
    return render(request, 'wish/wish_detail.html', {'wish': wish})
