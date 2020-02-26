from django.db import models

# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=255,)
    region = models.CharField(max_length=255,)
    score = models.IntegerField()
    rank = models.CharField(max_length=255,)
    image = models.ImageField(upload_to='images')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name