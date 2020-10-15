from django.db import models
from django.urls import reverse


class Pet(models.Model):

    DOG = 'Dog'
    CAT = 'Cat'
    PARROT = 'Parrot'
    UNKNOWN = 'Unknown'

    PET_TYPES_CHOICES = (
        (DOG, 'Dog'),
        (CAT, 'Cat'),
        (PARROT, 'Parrot'),
        (UNKNOWN, 'Unknown'),
    )

    type = models.CharField(max_length=6, choices=PET_TYPES_CHOICES, default=UNKNOWN)
    name = models.CharField(max_length=6)
    age = models.IntegerField(default=0)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('petstagram:pet_detail', kwargs={'id': self.id})


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('petstagram:pet_like', kwargs={'id': self.id})