from django.db import models
from polymorphic.models import PolymorphicModel


class Animals(PolymorphicModel):
    breed = models.CharField(max_length=30)

    def __str__(self):
        return self.breed

class Cat(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__

class Dog(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__

class Bird(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__

class Fish(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__

class Bear(Animals):
    name = models.CharField(max_length=30)
    abilities = models.CharField(max_length=255)
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.__class__.__name__

class ImageAnimals(models.Model):
    img = models.ImageField(upload_to='images')
    animal = models.ForeignKey(
        'Animals',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return  self.__class__.__name__