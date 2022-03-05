from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    ean = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    highlights = models.TextField(null=True)
    feature1 = models.CharField(max_length=254, null=True, blank=True)
    feature2 = models.CharField(max_length=254, null=True, blank=True)
    feature3 = models.CharField(max_length=254, null=True, blank=True)
    feature4 = models.CharField(max_length=254, null=True, blank=True)
    instock = models.CharField(max_length=254, null=True, blank=True)
    discount = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name