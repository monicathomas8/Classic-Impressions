from decimal import Decimal
from django.conf import settings
from catalogue.models import Product


class Cart:
    """
    Session-based shopping cart.
    This can be reused across projects without needing a Cart model.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("cart")

        if cart is None:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                # store as string for JSON serialisation
                "price": str(product.price),
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """
        Mark the session as modified so it will be saved.
        """
        self.session.modified = True

    def __iter__(self):
        """
        Iterate over the items in the cart and attach real Product objects.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            item = cart[str(product.id)]
            item["product"] = product
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        """
        Get the total cost of the cart.
        """
        return sum(
            Decimal(item["price"]) * item["quantity"]
            for item in self.cart.values()
        )

    def clear(self):
        """
        Remove cart from session.
        """
        if "cart" in self.session:
            del self.session["cart"]
            self.save()
