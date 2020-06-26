from django.db import models

class Base(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)


class ChildA(Base):

    def __str__(self):
        return  self.__class__.__name__

class ChildB(Base):
    
    def __str__(self):
        return  self.__class__.__name__
