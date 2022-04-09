from django.contrib import admin

from .models import Product


# Example
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']

# Add the rest of admin models here
