from cms.models.pluginmodel import CMSPlugin
from django.contrib.auth.models import User
from cms.extensions import PageExtension
from cms.extensions import TitleExtension
from cms.extensions.extension_pool import extension_pool

from django.db import models

class CategoryPlugin(CMSPlugin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    date_of_birthday = models.DateTimeField()
    profile_image = models.ImageField(upload_to='profiles',)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class IconExtension(PageExtension):
    image = models.ImageField(upload_to='icons')

extension_pool.register(IconExtension)


class RatingExtension(TitleExtension):
    rating = models.IntegerField()

extension_pool.register(RatingExtension)