from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
import stripe
from django.conf import settings
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    cart = Cart(request)
    errors = []
    form_data = {}

    if request.method == "POST":
        if len(cart) == 0:
            return redirect("cart_detail")

        form_data = {
            "full_name": request.POST.get("full_name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "address_line1": request.POST.get("address_line1", "").strip(),
            "address_line2": request.POST.get("address_line2", "").strip(),
            "city": request.POST.get("city", "").strip(),
            "postcode": request.POST.get("postcode", "").strip(),
            "country": request.POST.get("country", "").strip(),
        }

        required_fields = [
            "full_name", "email", "address_line1",
            "city", "postcode", "country",
        ]
        for field in required_fields:
            if not form_data[field]:
                field_name = field.replace('_', ' ').title()
                errors.append(f"{field_name} is required.")

        if errors:
            return render(request, "orders/checkout.html", {
                "cart": cart,
                "errors": errors,
                "form_data": form_data,
            })

        # Create Stripe payment intent
        total_amount = sum(
            item["price"] * item["quantity"] for item in cart
        )
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),
            currency="gbp",
            metadata={"email": form_data["email"]},
        )

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
            stripe_payment_intent=intent.id,
        )

        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item["product"],
                quantity=item["quantity"],
                price=item["price"],
            )

        cart.clear()

        # Send confirmation email to customer
        message = (
            f"Hi {order.full_name},\n\n"
            f"Thank you for your order!\n\n"
            f"Order #{order.id} has been received and we will be "
            f"in touch shortly.\n\n"
            f"Thank you for shopping with Classic Impressions."
        )
        send_mail(
            f"Order Confirmation - Classic Impressions #{order.id}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
        )

        return redirect("order_success", order_id=order.id)

    # GET request
    total_amount = sum(
        item["price"] * item["quantity"] for item in cart
    )
    intent = stripe.PaymentIntent.create(
        amount=int(total_amount * 100),
        currency="gbp",
    )
    return render(request, "orders/checkout.html", {
        "cart": cart,
        "errors": errors,
        "form_data": form_data,
        "stripe_publishable_key": settings.STRIPE_PUBLISHABLE_KEY,
        "client_secret": intent.client_secret,
    })


def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/order_success.html", {"order": order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "orders/my_orders.html", {"orders": orders})
