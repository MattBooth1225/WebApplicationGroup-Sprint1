from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User
from store.models import Profile


def order_create(request):
    cart = Cart(request)
    try:
        if User.is_authenticated:
            profile = request.user.profile
            if request.method == 'POST':
                form = OrderCreateForm(instance=profile)
                order = Order(first_name=profile.profile_fname,
                              last_name=profile.profile_lname,
                              email=profile.profile_email,
                              address=profile.profile_addressMain,
                              zip_code=profile.profile_zipcode,
                              city=profile.profile_city,
                              paid=True)
                order.save()
                cart.clear()
                return render(request, 'orders/order/created.html',
                                  {'order': order})
            else:
                form = OrderCreateForm(instance=profile)
                return render(request, 'orders/order/checkout.html',
                              {'cart': cart, 'form': form, 'profile': profile})
    except:

        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            order = Order(paid=True,
                          first_name='Guest',
                          last_name='Checkout')
            if form.is_valid():
                order.fname = form.cleaned_data['profile_fname']
                order.lname = form.cleaned_data['profile_lname']
                order.email = form.cleaned_data['profile_email']
                order.address = form.cleaned_data['profile_addressMain']
                order.zipcode = form.cleaned_data['profile_zipcode']
                order.city = form.cleaned_data['profile_city']
            order.save()
            cart.clear()
            return render(request, 'orders/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm()
            return render(request, 'orders/order/checkout.html',
                          {'cart': cart, 'form': form})












def order_create2(request):
    cart = Cart(request)
    try:
        if User.is_authenticated:
            profile = request.user.profile
            if request.method == 'POST':
                form = OrderCreateForm(instance=profile)
                if form.is_valid():
                    order = form.save()
                    for item in cart:
                        OrderItem.objects.create(order=order,
                                                 product=item['product'],
                                                 price=item['price'],
                                                 quantity=item['quantity'])
                    cart.clear()
                    return render(request, 'orders/order/created.html',
                                  {'order': order})
            else:
                form = OrderCreateForm(instance=profile)
                return render(request, 'orders/order/checkout.html',
                              {'cart': cart, 'form': form, 'profile': profile})
    except:

        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()
                return render(request, 'orders/order/created.html',
                              {'order': order})
        else:
            form = OrderCreateForm()
            return render(request, 'orders/order/checkout.html',
                          {'cart': cart, 'form': form})
