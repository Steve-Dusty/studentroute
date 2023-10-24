from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    school = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.user.email

class Driver(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.user.email

class Rider(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, default=False)

    def __str__(self):
        return self.profile.user.email

class Post(models.Model):
    frequency = models.CharField(max_length=255)
    time = models.TimeField()
    date = models.DateField()
    additional_info = models.TextField()
    rider = models.OneToOneField(Rider, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.rider.profile.user.email
