from django.contrib import admin

from .models import Seller,Vehicle,VehicleModel

admin.site.register(Seller)
admin.site.register(Vehicle)
admin.site.register(VehicleModel)
