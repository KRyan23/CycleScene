from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ean',
        'highlights',
        'feature1',
        'feature2',
        'feature3',
        'feature4',
        'category',
        'instock',
        'discount',
        'price',
        'description',
        'rating',
        'image1',
        'image2',
        'image3'
    )

    ordering = ('name', 'category', 'rating', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
