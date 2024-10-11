from django.urls import path
from . import views
from .views import current_weather, handle_user_location

urlpatterns = [
    path('', views.current_weather, name='current_weather'),
    path('?location_search=<location_search>', views.current_weather, name='location_search'),
    path('handle_user_location/', handle_user_location, name='handle_user_location'),
]