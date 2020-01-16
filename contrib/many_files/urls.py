from django.urls import path

from .views import files

urlpatterns = [
    path('', files, name='files'),
]
