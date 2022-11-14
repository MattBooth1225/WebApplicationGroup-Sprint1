from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from cart.forms import CartAddProductForm


def index(request):
    num_products = Product.objects.count()
    num_instances = ProductInstance.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_products': num_products,
        'num_instances': num_instances,
    }

    return render(request, 'index.html', context=context)


class AllProductsListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def music_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_music_list.html',
                  {'all-music': product})


def merch_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_merch_list.html',
                  {'all-merch': product})


def contact_us(request):
    if request.method == 'POST':
        contact_us = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact_us.name = name
        contact_us.email = email
        contact_us.message = message
        contact_us.save()

    return render(request, 'contactus.html')


# Sale Items Page
def sale_items(request):
    product = Product.objects.filter()
    return render(request, 'store/sale_items.html',
                  {'sale-items': product})


def wish_list(request):
    product = Product.objects.filter()
    return render(request, 'store/wish_list.html',
                  {'wish-list': product})


# --------------------------------------------------
#  User Account Views
# --------------------------------------------------
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'], )
            login(response, new_user)

        return redirect("/store")
    else:
        form = RegisterForm()

    return render(response, "registration/user_registration.html", {"form": form})


# I want to change this to import the user instead of the product but I am not sure what pycharm calls the user class
def user_profile_settings(request):
    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_settings.html',
                  {'user-profile-settings': profile})


def user_profile_shipping_address(request):
    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_shipping_address.html',
                  {'user-profile-shipping-address': profile})


def user_profile_payment_methods(request):
    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_payment_methods.html',
                  {'user-profile-payment-methods': profile})


def user_profile_order_history(request):
    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_order_history.html',
                  {'user-profile-order-history': profile})


def shopping_cart(request):
    product = Product.objects.filter()
    return render(request, 'store/shopping_cart.html',
                  {'shopping-cart': product})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product_detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


