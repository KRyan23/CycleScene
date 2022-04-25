from django.db import models

# Rating choices dropdown list to tie in with ratings.js
RATING_CHOICES = (
        (0.5,'0.5'),
        (1, '1'),
        (1.5,'1.5'),
        (2,'2'),
        (2.5,'2.5'),
        (3,'3'),
        (3.5,'3.5'),
        (4,'4'),
        (4.5,'4.5'),
        (5,'5'),
    )


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
    ean = models.CharField(max_length=254, null=True, blank=False)
    name = models.CharField(max_length=254, null=True, blank=False)
    highlights = models.TextField(null=True, blank=False)
    feature1 = models.CharField(max_length=254, null=True, blank=False)
    feature2 = models.CharField(max_length=254, null=True, blank=False)
    feature3 = models.CharField(max_length=254, null=True, blank=False)
    feature4 = models.CharField(max_length=254, null=True, blank=False)
    instock = models.BooleanField(default=True)
    discount = models.BooleanField(default=False)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=5, decimal_places=1,
    choices=RATING_CHOICES, null=True, blank=True, default="5")
    image1 = models.ImageField(null=True, blank=False)
    image2 = models.ImageField(null=True, blank=False)
    image3 = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name
