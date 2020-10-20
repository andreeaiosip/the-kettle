from django.contrib import admin
from .models import Product, Category, Ingredient, Flavour


# Register your models here.

# Product Model

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
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


# Ingredients Model


class IngredientAdmin(admin.ModelAdmin):
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
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Flavour, FlavourAdmin)
