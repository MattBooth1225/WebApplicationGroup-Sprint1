from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product, Profile
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})
    return render(request, 'cart/detail.html', {'cart': cart})


def checkout(request):
    cart_checkout = Cart(request)
    return render(request, 'checkout.html', {'cart': cart_checkout})


def get_profile(request):
    try:
        profile = request.user.profile

    except:
        profile = Profile()

    context = {
        'profile_email': profile.profile_email,
        'profile_fname': profile.profile_fname,
        'profile_lname': profile.profile_lname,
        'profile_addressMain': profile.profile_addressMain,
        'profile_city': profile.profile_city,
        'profile_state': profile.profile_state,
        'profile_zipcode': profile.profile_zipcode
    }

    return render(request, 'orders/order/checkout.html', context)
