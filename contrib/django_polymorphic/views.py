from django.shortcuts import render

from rest_framework import viewsets
from .models import Animals

from .serializers.animals_polymorphic_serializer import AnimalsPolymorphicSerializer, CatSerializer,\
                                                    DogSerializer, BearSerializer, BirdSerializer,\
                                                    FishSerializer

class AminalsViewSet(viewsets.ModelViewSet):
    queryset = Animals.objects.all()
    serializer_class = AnimalsPolymorphicSerializer
