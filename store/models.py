from django.db import models
from django.urls import reverse
import uuid
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.forms import ModelForm


# Newsletter Class
class Newsletter(models.Model):
    newsletter_id = models.IntegerField(primary_key=True, unique=True)
    message = models.TextField(max_length=1000)


class Category(models.Model):
    name = models.CharField(primary_key=True,
                            max_length=200)  # instead of using a number to identify categories, the name might be easier, can change in future if it isnt
    slug = models.SlugField(max_length=200, unique=True)

    # img I am not sure how to implement this -- after more research we may need a plugin for this, will look into it later
    # Categories should be functional

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


# Product Related Classes
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)  # Want to change to more specific field for cost in future
    desc = models.TextField(blank=True)
    sale = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, blank=True, null=True)

    def saleprice(self):
        if self.sale == True:
            tempPrice = float(self.price) * 0.75
            return tempPrice

    # Adding Type as test for future use; want to use it sort categories
    # type = models.TextField(max_length=200)

    # img I am not sure how to implement this

    # New method for searching for type in lists
    # def search_type(self):
    # if self.type == "Music":
    # return self.type
    # elif self.type == "Merch":
    # return self.type
    # else:
    # type_not_found = "Type Not Found"
    # return type_not_found

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

        # Returns the URL to access a detail record for this book

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.id, self.slug])


class ProductInstance(models.Model):
    instance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='A unique ID for this particular'
                                                                                   'product across the whole store')
    product = models.ForeignKey('Product', on_delete=models.RESTRICT, null=True)
    sold_status = models.BooleanField()

    def __str__(self):
        return f'{self.product_id} ({self.product.name})'


class ShoppingCart(models.Model):
    shoppingcart_id = models.UUIDField(primary_key=True)
    total = models.DecimalField(max_digits=9,
                                decimal_places=2)  # Want to change to more specific field for cost in future
    quantity = models.IntegerField()  # should be good just an integer field to display how many products there are in the cart
    products = models.ManyToManyField(Product)  # right now we select the products for each cart
    user_cart = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  null=True)  # Probably needs to be changed-- looks good now


class WishList(models.Model):
    wishlist_id = models.UUIDField(primary_key=True)
    total = models.IntegerField()  # Want to change to more specific field for cost in future
    quantity = models.IntegerField()


# Currently trying to use Profile Class as way to edit more in depth user information
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=200, default="a@a")
    profile_fname = models.CharField(max_length=200, default="firstname")
    profile_lname = models.CharField(max_length=200, default="lastname")
    profile_addressMain = models.CharField(max_length=200, default="a")
    profile_addressSecondary = models.CharField(max_length=200, blank=True)
    profile_city = models.CharField(max_length=200, default="Omaha")
    profile_state = models.CharField(max_length=2, default="NE")
    profile_zipcode = models.IntegerField(default=68022)


# Form for changing settings on profile_settings page
class ProfileSettingsForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_email', 'profile_fname', 'profile_lname']


class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)


class Order(models.Model):
    order_id = models.CharField(primary_key=True, max_length=15)
    date = models.DateField(auto_now=True)
    items = models.ManyToManyField(OrderItem)

    # total = models.IntegerField()  # Want to change to more specific field for cost in future
    # quantity = models.IntegerField()
    # Code Below Probably needs to be changed
    # shoppingcart_id = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # wishlist_id = models.ForeignKey(WishList, on_delete=models.CASCADE)

    def get_cart_items(self):
        return self.items.all()

    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])


class Payment(models.Model):
    payment_id = models.UUIDField(primary_key=True)
    cardnum = models.IntegerField()  # Want to change to more specific field for card in future
    exp = models.DateField(null=True, blank=True)
    securitycode = models.IntegerField()  # removed max length to make an error code happy
    member_username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Contact(models.Model):
    name = models.CharField(max_length=158)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
