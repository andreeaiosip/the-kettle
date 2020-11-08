from django.contrib import admin
from .models import Article

# Register your models here.
 
 # Article Model


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'pub_date',
        'body',
    )

    ordering = ('pub_date',)


admin.site.register(Article, ArticleAdmin)
