from django.db import models


class Category(models.Model):

    """
    Represents a group or collection of products
    (e.g. Lighting, Mirrors, Sculptures).
    Categories help organise the shop and make filtering easier.
    Each category has a unique name and slug so it can be used in URLs.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    A base product model for your reusable e-commerce template.
    This stores general product information, linked to a category.
    Designed to be expanded later with custom fields depending on the client.
    """
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    unlimited_stock = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
