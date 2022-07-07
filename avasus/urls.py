from django.urls import path

from . import views 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:avasus_id>', views.avasus, name='avasus'),
    path('buscar', views.buscar, name='buscar')
]