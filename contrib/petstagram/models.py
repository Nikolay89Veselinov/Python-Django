from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User


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
    slug = models.SlugField(editable=False)
    type = models.CharField(max_length=6, choices=PET_TYPES_CHOICES, default=UNKNOWN)
    name = models.CharField(max_length=6)
    age = models.IntegerField(default=0)
    description = models.TextField()
    image_url = models.ImageField(upload_to='images/pets')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('petstagram:pet_detail', kwargs={'pk': self.id})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('petstagram:pet_like', kwargs={'pk': self.id})


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
