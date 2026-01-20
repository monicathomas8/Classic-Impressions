from django.contrib import admin
from .models import CustomServiceRequest


@admin.register(CustomServiceRequest)
class CustomServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'request_type', 'status', 'created_at')
    list_filter = ('request_type', 'status', 'created_at')
    search_fields = ('name', 'email', 'description', 'budget')
    readonly_fields = (
        'name', 'email', 'phone', 'request_type', 'description',
        'budget', 'preferred_date', 'created_at'
    )
    ordering = ('-created_at',)
