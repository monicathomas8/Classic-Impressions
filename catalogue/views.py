from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    """
    Basic homepage that lists all active products.
    This will act as the first simple shop
    view for your e-commerce base.
    """
    products = Product.objects.filter(
        is_active=True
    ).select_related('category')
    context = {
        'products': products,
    }
    return render(request, 'catalogue/products.html', context)


def product_detail(request, slug):
    """
    A simple product detail view.
    Fetches a product by its slug and displays its details.
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    context = {
        'product': product,
    }
    return render(request, 'catalogue/product_detail.html', context)
