from django.db import models

class Notification(models.Model):
    type_notification = models.CharField(max_length=255)
    message = models.CharField(max_length=512)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.type_notification
