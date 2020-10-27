from django.contrib import admin
from .models import Product, Category, Flavour


# Register your models here.

# Product Model

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'flavour',
        'name',
        'price',
    )

    ordering = ('category',)


# Category Model

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',
    )


# Flavour Model

class FlavourAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flavour, FlavourAdmin)
