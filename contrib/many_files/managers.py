from django.db import models


class MyManager(models.Manager):
    def всички(self):
        return self.all()
