from decimal import Decimal
from django.conf import settings
from store.models import Product


class Wishlist(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        wish = self.session.get(settings.WISH_SESSION_ID)
        if not wish:
            # save an empty cart in the session
            wish = self.session[settings.WISH_SESSION_ID] = {}
        self.wish = wish

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.wish.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)

        wish = self.wish.copy()
        for product in products:
            wish[str(product.id)]['product'] = product

        for item in wish.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']  # removed * item['quantity'] after ['price']
            yield item

    def __len__(self):

        # Count all items in the cart.

        return sum(item['quantity'] for item in self.wish.values())  # should I create a for loop for item[]

    def add(self, product, quantity=1, override_quantity=False):

        # Add a product to the cart or update its quantity.

        product_id = str(product.id)
        if product_id not in self.wish:
            self.wish[product_id] = {'quantity': 0, 'price': str(product.price)}

        if override_quantity:
            self.wish[product_id]['quantity'] = quantity
        else:
            self.wish[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.wish:
            del self.wish[product_id]
            self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.wish.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.WISH_SESSION_ID]
        self.save()
