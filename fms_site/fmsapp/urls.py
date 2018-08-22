from django.urls import path
from . import views

app_name = 'fmsapp' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
]
