from django.urls import path
from . import views

urlpatterns = [
    path('', views.current_weather, name='current_weather'),
    path('?location_search=<location_search>', views.current_weather, name='location_search'),
    path('user_location/', views.current_weather, name='handle_user_location'),
]
