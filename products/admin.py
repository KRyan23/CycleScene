from django.contrib import admin
from .models import Product, Category
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ean',
        'highlights',
        'frame',
        'fork',
        'groupset',
        'wheels',
        'category',
        'instock',
        'discount',
        'price',
        'description',
        'rating',
        'image'
    )

    ordering = ('name', 'category', 'rating', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
