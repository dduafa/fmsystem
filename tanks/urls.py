from django.urls import path
from .views import (
    create_tank_view,
    signup
)

app_name = 'tanks'
urlpatterns = [
    path('signups/', signup, name='signup'),
    path('createtank/', create_tank_view, name='create_tank'),
]
