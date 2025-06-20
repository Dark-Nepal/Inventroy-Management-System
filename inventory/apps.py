from django.apps import AppConfig


class InventoryAppConfig(AppConfig): 
    name = 'inventory'  
    

    def ready(self):
        import inventory.signals 
