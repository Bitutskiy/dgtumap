from django.shortcuts import render
from rest_framework import generics
from .serializers import ObjectSerializer, Objects


def index(request):
    return render(request, 'geolocation/main_page.html')


def map_page(request):
    return render(request, 'geolocation/map.html')


class ObjectsListView(generics.ListAPIView):
    serializer_class = ObjectSerializer
    queryset = Objects.objects.all()
