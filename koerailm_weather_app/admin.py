from django.contrib import admin
from .models import WeatherData, FavouritePlace, UserFeedback, FolkSaying

admin.site.register(WeatherData)
admin.site.register(FavouritePlace)
admin.site.register(UserFeedback)
admin.site.register(FolkSaying)
