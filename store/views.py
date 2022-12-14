from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import *
from .forms import *
from cart.forms import CartAddProductForm


def index(request):
    num_products = Product.objects.count()
    num_instances = ProductInstance.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_products': num_products,
        'num_instances': num_instances,
        'images': [
            'SOAD_Steal_This_Album_CD.jpg',
            'Beartooth_Disgusting_Shirt.JPG',
            'GreenDay_American_Idiot_CD.jpg',
            'MCR_Black_Parade_Shirt.jpg',
            'MCR_Three_Cheers_Shirt.jpg',
            'Northernaire_Vinyl.jpg',
        ],
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
                  'store/all_products.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        search_results = Product.objects.filter(name__contains=searched)

        return render(request, 'store/search_products.html', {'searched': searched, 'search_results': search_results})
    else:
        return render(request, 'store/search_products.html', {})


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

        return redirect("/music")
    else:
        form = RegisterForm()

    return render(response, "registration/user_registration.html", {"form": form})


def user_profile_settings(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            user_profile = Profile.objects.get(pk=current_user)
        except:
            user_profile = Profile()
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        user_profile.user = current_user
        user_profile.profile_email = email
        user_profile.profile_fname = fname
        user_profile.profile_lname = lname
        try:
            user_profile.save()
        except:
            user_profile.save(force_update=True)

    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_settings.html',
                  {'user-profile-settings': profile})


# def user_profile_valid(self, form):
# form.instance.user = self.kwargs.get('pk')
# return super()

def user_profile_shipping_address(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            user_profile = Profile.objects.get(pk=current_user)
        except:
            user_profile = Profile()
        profile_address1 = request.POST.get('address1')
        profile_address2 = request.POST.get('address2')
        profile_city = request.POST.get('city')
        profile_state = request.POST.get('state')
        profile_zip = request.POST.get('zipcode')
        user_profile.user = current_user
        user_profile.profile_addressMain = profile_address1
        user_profile.profile_addressSecondary = profile_address2
        user_profile.profile_city = profile_city
        user_profile.profile_state = profile_state
        user_profile.profile_zipcode = profile_zip
        try:
            user_profile.save()
        except:
            user_profile.save(force_update=True)

    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_shipping_address.html',
                  {'user-profile-shipping-address': profile})


# working on payment method view here...

def user_profile_payment_methods(request):
    if request.method == 'POST':
        current_user = request.user
        try:
            user_profile = Profile.objects.get(pk=current_user)
        except:
            user_profile = Profile()
        profile_cardnum = request.POST.get('cardnum')
        profile_exp = request.POST.get('exp')
        profile_security = request.POST.get('security')

        user_profile.user = current_user

        user_profile.profile_cardnum = profile_cardnum
        user_profile.profile_sec_code = profile_security
        user_profile.profile_exp_date = profile_exp

        try:
            user_profile.save()
        except:
            user_profile.save(force_update=True)

    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_payment_methods.html',
                  {'user-profile-payment': profile})


# def user_profile_payment_methods(request):
# profile = Profile.objects.filter()
# return render(request, 'registration/user_profile_payment_methods.html',
# {'user-profile-payment-methods': profile})


def user_profile_order_history(request):
    profile = Profile.objects.filter()
    return render(request, 'registration/user_profile_order_history.html',
                  {'user-profile-order-history': profile})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'store/product_detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


def merch(request, slug):
    category = get_object_or_404(Category, slug=merch)
    return render(request, 'store/all_merch_list.html',
                  {'category': category})
