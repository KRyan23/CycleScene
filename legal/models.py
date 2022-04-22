'''Required Imports'''
from django.db import models


class Legal(models.Model):
    '''Register all models with the correct field types'''
    name = models.CharField(max_length=254, null=True, blank=False)
    titleprivacypolicy = models.CharField(max_length=254, null=True, blank=False)
    bodyprivacypolicy = models.TextField(default=True, null=False, blank=True)
    titletermsandconditions = models.CharField(max_length=254, null=True, blank=False)
    bodytermsandconditions = models.TextField(default=True, null=False, blank=True)
    titlereturnspolicy= models.CharField(max_length=254, null=True, blank=False)
    bodyreturnspolicy = models.TextField(default=True, null=False, blank=True)


    def __str__(self):
        return self.name
