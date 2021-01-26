from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from .models import  UsersProfile
from .forms import SignUpForm, UsersProfileForm



def user_profile(request, id=None):
    user = request.user if id is None else User.objects.get(pk=id)
    # import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        context = {
            'user': user,
            'pets': user.pet_set.all(),
            'profile': UsersProfile.objects.get(user_id=user.id),
            'form': UsersProfileForm(),
        }

        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UsersProfileForm(request.POST, request.FILES, instance=UsersProfile.objects.get(user_id=user.id))
        if form.is_valid():
            form.save()
            return redirect('accounts:current_user_profile')

def sign_up(request):
    if request.method == 'GET': 
        context = {
            'form': SignUpForm()
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UsersProfile(
                user=user,
            )
            profile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('accounts:current_user_profile')

        context = {
            'form': form
        }

        return render(request, 'accounts/signup.html', context)

class SignUpViews(views.CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:current_user_profile')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return valid

def signout_user(request):
    logout(request)
    return redirect('petstagram:landing_page')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('petstagram:landing_page')


class SignInView(auth_views.LoginView):
    template_name = 'registration/login.html'
