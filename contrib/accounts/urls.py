from django.urls import path
from django.conf.urls import include, url

from .views import user_profile, sign_up, signout_user
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'accounts'


urlpatterns = [
    path('singin/', LoginView.as_view(), name="login"),
    path('signout/', signout_user, name="signout_user"),
    path('profile/', user_profile, name='current_user_profile'),
    path('profile/<int:id>/', user_profile, name='user_profile'),
    path('signupacc/', sign_up, name='sign_up'),
]