from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

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
            return redirect('petstagram:landing_page')

        context = {
            'form': form
        }

        return render(request, 'accounts/signup.html', context)

def signout_user(request):
    logout(request)
    return redirect('petstagram:landing_page')