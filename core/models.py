from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    address = models.TextField()
    is_driver = models.BooleanField()

class Post(models.Model):
    frequency = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    additional_info = models.TextField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Pair(models.Model):
    driver = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="driver")
    rider = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="rider")
