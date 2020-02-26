from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer, ItemSerializer
from .models import Item

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer