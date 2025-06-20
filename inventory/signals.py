from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseItem, SaleItem, Product, StockMovement

@receiver(post_save, sender=PurchaseItem)
def update_stock_on_purchase(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity += instance.quantity
        product.save()

        StockMovement.objects.create(
            product=product,
            change_type='in',
            reference_id=instance.purchase.id,
            source_table='purchases',
            quantity=instance.quantity
        )

@receiver(post_save, sender=SaleItem)
def update_stock_on_sale(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.quantity -= instance.quantity
        product.save()

        StockMovement.objects.create(
            product=product,
            change_type='out',
            reference_id=instance.sale.id,
            source_table='sales',
            quantity=instance.quantity
        )
