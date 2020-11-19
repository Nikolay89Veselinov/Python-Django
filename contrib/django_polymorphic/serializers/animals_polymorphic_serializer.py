from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer
from contrib.django_polymorphic.models import Animals, Cat, Dog, Bird, Fish, Bear, ImageAnimals


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'abilities', 'age')


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'abilities', 'age')


class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = ('name', 'abilities', 'age')


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = ('name', 'abilities', 'age')


class BearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bear
        fields = ('name', 'abilities', 'age')

class ImageAnimalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageAnimals
        fields = ('img', 'animals')

class AnimalsPolymorphicSerializer(PolymorphicSerializer):
    """A class that assigns the correct serializer class to an asset of a certain type."""

    model_serializer_mapping = {
        Cat: CatSerializer,
        Dog: DogSerializer,
        Bird: BirdSerializer,
        # Fish: FishSerializer,
        Bear: BearSerializer,
        ImageAnimals: ImageAnimalsSerializer,
    }
