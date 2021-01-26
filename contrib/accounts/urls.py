from django.urls import path
from django.conf.urls import include, url

from .views import SignInView, SignOutView, user_profile, sign_up, signout_user, SignUpViews
from django.contrib.auth.views import LoginView, LogoutView 

app_name = 'accounts'


urlpatterns = [
    # path('singin/', LoginView.as_view(), name="login"),
    path('singin/', SignInView.as_view(), name="login"),
    # path('signout/', signout_user, name="signout_user"),
    path('signout/', SignOutView.as_view(), name="signout_user"),
    path('profile/', user_profile, name='current_user_profile'),
    path('profile/<int:id>/', user_profile, name='user_profile'),
    # path('signupacc/', sign_up, name='sign_up'),
    path('signupacc/', SignUpViews.as_view(), name='sign_up'),

]

from .receviers import *