from django.db import models
from django.contrib.auth.models import User


class UsersProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profiles', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user