from django.db import models


class WeatherData(models.Model):
    location_id = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    condition = models.CharField(max_length=50)
    timestamp = models.DateTimeField()


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField()

    def __str__(self):
        return self.username


class FavouritePlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)
    rank = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.place_name} (Rank {self.rank})"


class UserFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback submitted by {self.user.username} on {self.submitted_at}"


class FolkSaying(models.Model):
    folk_saying = models.TextField()

    def __str__(self):
        return self.folk_saying
