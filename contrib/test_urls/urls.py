from django.urls import path


from .views import monthly_challenge, monthly_challenge_by_numbers

app_name = 'challenge'


urlpatterns = [
    path('<str:month>/', monthly_challenge, name='month-challenge'),
    path('num/<int:month>/', monthly_challenge_by_numbers, name='month-challenge-by-numbers'),
]