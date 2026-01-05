from django.db import models
from django.conf import settings
from catalogue.models import Product


class Order(models.Model):
    """
    A basic order model that can be reused across projects.
    You can extend this later with shipping details, payment info, etc.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True,
        blank=True
    )

    # Basic customer / shipping details
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # simple status to start with - can extend later
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSING', 'Processing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
    )

    def __str__(self):
        return f"Order #{self.id} ({self.status})"

    def total_items(self):
        """
        Total number of items in this order.
        """
        return sum(item.quantity for item in self.items.all())
    total_items.short_description = "Items"

    def total_amount(self):
        """
        Total value of this order.
        """
        return sum(item.quantity * item.price for item in self.items.all())
    total_amount.short_description = "Total (£)"


class OrderItem(models.Model):
    """
    A single line item within an order, linked to a product.
    """
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items',
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} "
            f"(order #{self.order.id})"
        )
