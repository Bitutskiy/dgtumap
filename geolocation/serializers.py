from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Objects


class ObjectSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Objects
        geo_field = "geom"
        fields = ('pk', 'name', 'description', 'type')
