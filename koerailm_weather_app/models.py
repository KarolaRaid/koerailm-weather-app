from django.db import models
from django.contrib.auth.models import User


class WeatherData(models.Model):
    location_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    condition = models.CharField(max_length=50)
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Weather data for location {self.location_id} on {self.timestamp}"


class FavouritePlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rank = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Rank {self.rank})"


class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback submitted by {self.user.username} on {self.submitted_at}"


class FolkSaying(models.Model):
    text = models.TextField()
    month = models.IntegerField()

    def __str__(self):
        return self.text
