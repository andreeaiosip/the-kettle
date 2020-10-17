from django.contrib import admin
from .models import Coffee, Tea


# Register your models here.
class CoffeeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'strength',
        'price',
    )

    ordering = ('strength',)


class TeaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'tea_bags',
        'ingredients',
        'price',
    )
    ordering = ('price',)


admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Tea, TeaAdmin)
