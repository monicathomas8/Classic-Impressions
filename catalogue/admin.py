from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "thumbnail",
        "name",
        "category",
        "price",
        "stock",
        "unlimited_stock",
        "is_active",
        "created_at",
    )
    list_filter = ("is_active", "category")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}

    def thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" '
                'style="object-fit: cover; border-radius: 4px;" />',
                obj.image.url,
            )
        return "-"

    readonly_fields = ("image_preview",)
    fields = (
        "name",
        "slug",
        "category",
        "price",
        "description",
        "image",
        "image_preview",
        "stock",
        "unlimited_stock",
        "is_active",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="200" style="border-radius: 6px;" />',
                obj.image.url,
            )
        return "No image uploaded yet."
