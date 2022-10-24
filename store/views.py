from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *


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


def music_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_music_list.html',
                  {'all-music': product})

def merch_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_merch_list.html',
                  {'all-merch': product})

def contact_us(request):
    return render(request, 'contactus.html')

#def cart_add(request, prod_id):
    #finds the profile of the user who clicked add to cart
    #user_profile = get_object_or_404(Profile, user=request.user)
    #gets the product by finding its ID
    #product = Product.objects.get(prod_id=prod_id)
    #cart = ShoppingCart(request)

# def removeFromCart(request):

#Sale Items Page
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
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            login(response, new_user)

        return redirect("/store")
    else:
        form = RegisterForm()

    return render(response, "registration/user_registration.html", {"form": form})


# I want to change this to import the user instead of the product but I am not sure what pycharm calls the user class
def user_profile_settings(request):
    product = Product.objects.filter()
    return render(request, 'registration/user_profile_settings.html',
                  {'user-profile-settings': product})