from .cart import Cart


def cart_item_count(request):
    """
    Make the cart item count available in all templates.
    """
    cart = Cart(request)
    return {
        "cart_items_count": len(cart)
    }
