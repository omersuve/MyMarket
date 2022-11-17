from django.contrib import admin
from .models import Store, Product


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
    )


admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
