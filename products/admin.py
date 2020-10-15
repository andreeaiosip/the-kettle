from django.contrib import admin
from .models import Coffee, Tea


# Register your models here.
class CoffeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'strength',
        'image',
        'price',
    )

    ordering = ('strength',)


class TeaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ingredients',
        'tea_bags',
        'image',
        'price',
    )
    ordering = ('price',)


admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Tea, TeaAdmin)
