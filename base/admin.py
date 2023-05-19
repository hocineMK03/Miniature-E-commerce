from django.contrib import admin
from core.models import Customers,Product,Category,Session_model,CategoryofCategories,Order
# Register your models here.

admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Session_model)
admin.site.register(CategoryofCategories)
admin.site.register(Order)