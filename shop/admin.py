from django.contrib import admin
from .models import Product, Contact, Order, OrderUpdate

# Register your models here(To show model in admin!)
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)
