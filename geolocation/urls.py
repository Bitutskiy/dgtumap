from django.urls import path

from . import views

appname = 'geolocation'
urlpatterns = [
    path('map/', views.map_page, name='map_page'),
    path('map/data', views.ObjectsListView.as_view()),
    path('', views.index, name='index')
]
