from django.urls import path

from contrib.home.views import url_with_arguments

car = {
    'Mercedes-Benz': 'Mercedes-Benz C320cdi',
    'BMW': 'BMW 330xi',
}

urlpatterns = [
    path('', url_with_arguments, kwargs={'car': car}, name='url_with_arguments'),
    path('<str:username>/', url_with_arguments, {'car': 'Audi RS6'}, name='url_with_arguments'),
    path('<str:username>/<slug:article_value>/', url_with_arguments, name='url_with_arguments'),
    path('<str:username>/<slug:article_value>/<str:city_id>/', url_with_arguments, name='url_with_arguments'),
]
