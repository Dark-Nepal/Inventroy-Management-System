from django.contrib import admin
from .models import (
    Category, Supplier, Product,
    Purchase, PurchaseItem,
    Sale, SaleItem, StockMovement
)

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 1

class SaleItemInline(admin.TabularInline):
    model = SaleItem
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sku', 'category', 'price', 'quantity']
    search_fields = ['name', 'sku']
    list_filter = ['category']

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'supplier', 'purchase_date', 'total_amount', 'status']
    inlines = [PurchaseItemInline]
    list_filter = ['status']
    search_fields = ['supplier__name']

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'sale_date', 'total_amount', 'payment_type']
    inlines = [SaleItemInline]
    list_filter = ['payment_type']
    search_fields = ['customer_name']

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'change_type', 'quantity', 'source_table', 'reference_id', 'date']
    list_filter = ['change_type', 'source_table']
    search_fields = ['product__name', 'source_table']
# This code registers the models with the Django admin site, allowing for easy management of inventory data.