''' Required Imports '''
from django.db import models


class Service(models.Model):
    ''' Register all models with the correct field types '''
    name = models.CharField(max_length=254, null=True, blank=False)
    titlerepair = models.CharField(max_length=254, null=True, blank=False)
    bodyrepair = models.TextField(default=True, null=False, blank=True)
    titlerescue = models.CharField(max_length=254, null=True, blank=False)
    bodyrescue = models.TextField(default=True, null=False, blank=True)
    service1 = models.TextField(default=True, null=False, blank=True)
    service2 = models.TextField(default=True, null=False, blank=True)
    def __str__(self):
        return self.name
    