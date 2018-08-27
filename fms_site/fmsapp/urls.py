from django.urls import path
from . import views

app_name = 'fmsapp' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
    path('compare_address/', views.compare_address, name='compare_address'),
    path('display_address_on_map1/', views.display_address_on_map1, name='display_address_on_map1'),
    path('display_address_on_map2/', views.display_address_on_map2, name='display_address_on_map2'),
    path('resources/', views.resources, name='resources'),
]
