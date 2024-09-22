from django.contrib import admin
from .models import WeatherData, User, FavouritePlace, UserFeedback, FolkSaying

admin.site.register(WeatherData)
admin.site.register(User)
admin.site.register(FavouritePlace)
admin.site.register(UserFeedback)
admin.site.register(FolkSaying)
