from django.contrib import admin
from order.models import Order, Order_item

admin.site.register(Order)
admin.site.register(Order_item)
