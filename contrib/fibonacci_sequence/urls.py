from django.urls import path
from .views import get_fibonacci_number


app_name = 'fibonacci_number'


urlpatterns = [
    path('', get_fibonacci_number, name='fibonacci_number'),
]