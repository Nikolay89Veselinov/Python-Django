from django.urls import path

from contrib.home.views import url_with_arguments


urlpatterns = [
    path('', url_with_arguments, name='url_with_arguments'),
    path('<str:username>/', url_with_arguments, name='url_with_arguments'),
    path('<str:username>/<slug:article_value>/', url_with_arguments, name='url_with_arguments'),
    path('<str:username>/<slug:article_value>/<str:city_id>/', url_with_arguments, name='url_with_arguments'),
]
