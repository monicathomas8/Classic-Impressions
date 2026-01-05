from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required


def checkout(request):
    """
    Show checkout page and create an order from the cart on POST.
    """
    cart = Cart(request)
    errors = []
    form_data = {}

    if request.method == "POST":
        if len(cart) == 0:
            return redirect("cart_detail")

        # Grab fields from the form
        form_data = {
            "full_name": request.POST.get("full_name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "address_line1": request.POST.get("address_line1", "").strip(),
            "address_line2": request.POST.get("address_line2", "").strip(),
            "city": request.POST.get("city", "").strip(),
            "postcode": request.POST.get("postcode", "").strip(),
            "country": request.POST.get("country", "").strip(),
        }

        # Simple required field checks
        required_fields = [
            "full_name",
            "email",
            "address_line1",
            "city",
            "postcode",
            "country",
        ]
        for field in required_fields:
            if not form_data[field]:
                field_name = field.replace('_', ' ').title()
                errors.append(f"{field_name} is required.")

        if errors:
            # Re-render page with errors + form data
            context = {
                "cart": cart,
                "errors": errors,
                "form_data": form_data,
            }
            return render(request, "orders/checkout.html", context)

        # Create the order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            full_name=form_data["full_name"],
            email=form_data["email"],
            address_line1=form_data["address_line1"],
            address_line2=form_data["address_line2"],
            city=form_data["city"],
            postcode=form_data["postcode"],
            country=form_data["country"],
        )

        # Create order items from the cart
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                price=item["price"],
            )

        # Clear the cart
        cart.clear()

        return redirect("order_success", order_id=order.id)

    # GET request
    context = {
        "cart": cart,
        "errors": errors,
        "form_data": form_data,
    }
    return render(request, "orders/checkout.html", context)


def order_success(request, order_id):
    """
    Simple order confirmation page.
    """
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order_success.html", {"order": order})


@login_required
def my_orders(request):
    """
    Show a list of orders for the logged-in user.
    """
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/my_orders.html", {"orders": orders})
