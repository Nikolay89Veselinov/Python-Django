from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name += ' worldd'
        super(Country, self).save(*args, **kwargs)

    def 


class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Pub(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name


@receiver(post_save, sender=Country)
def initial_city(sender, **kwargs):
    if kwargs.get('created'):
        country = kwargs.get('instance')
        city = City(name='First city', country=country)
        city.save()


@receiver(post_save, sender=City)
def initial_pub(sender, **kwargs):
    if kwargs.get('created'):
        city = kwargs.get('instance')
        pub = Pub(name='First pub', city=city, active=True)
        pub.save()