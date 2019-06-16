from django.urls import path
from .views import (
    create_station_view,
)

app_name = 'stations'

urlpatterns = [
    path('createstation/', create_station_view, name='create_station'),
]