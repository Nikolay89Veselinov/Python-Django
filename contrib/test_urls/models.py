from django.db import models

class ASD(models.Model):
    title = models.CharField(max_length=333)
