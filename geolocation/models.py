from django.db import models
from django.contrib.gis.db import models as gismodels

# Create your models here.


class Types(models.Model):
    """
    Basic class for name of category with description
    """
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Objects(models.Model):
    """
    Class for geo objects
    """
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255)
    geom = gismodels.PointField()
    type = models.ForeignKey('Types', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

