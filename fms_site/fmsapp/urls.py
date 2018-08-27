from django.urls import path
from . import views

app_name = 'fmsapp' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
    path('compare_address/', views.compare_address, name='compare_address'),
    path('display_address_on_map/', views.display_address_on_map, name='display_address_on_map'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources, name='resources'),
]
