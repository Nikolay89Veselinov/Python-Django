from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import transaction

from contrib.form_wizard.models import Client
from contrib.sort_filter.models import City, Country, Pub
from contrib.based_views.forms import ArticleForm
from .forms import RegisterForm, UserCreationForm, ProfileForm, LoginForm

def get_redirect_url(params):
    redirect_url = params.get('return_url')
    return redirect_url if redirect_url else 'home'
    print('test git revert merge 1')
    print('test git revert merge 2')

def home(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    print('test git revert 2')
    if num_visits >= 5:
        del(request.session['num_visits'])
    context = {
        'view_count': ('view count ' + str(num_visits)),

    }
    
    return render(request, 'home.html', context)

def url_with_arguments(request, username='Default User', article_value='Default Article', city_id='Default ID', **kwargs):
    user = request.user

    if city_id != 'Default ID':
        city_id = City.objects.get(id=city_id)

    return HttpResponse(
        '<p>Write URL!!!</p>'
        f'<p>Username: {username}</p>'
        f'<p>Article: {article_value}</p>'
        f'<p>City: {city_id}</p>'
        f'<p>Login User: {user}</p>'
        f'<p>Cars: {kwargs}</p>'
    )

def reverse_views(request):
    city_id = ['Pesho', 'Pestrov', '1']
    return HttpResponseRedirect(reverse('url_with_arguments', args=(city_id)))


def dynamic_client(request, id, dele):

    obj = get_object_or_404(Client, pk=id)

    return HttpResponse(
        '<p>Write URL!!!</p>'
        f'<p>first_name: {obj.first_name}</p>'
        f'<p>last_name: {obj.last_name}</p>'
        f'<p>eng: {obj.eng}</p>'
        f'<p>phone: {obj.phone}</p>'
        f'<p>email: {obj.email}</p>'
    )

def template_tags(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    pubs = Pub.objects.filter(active=True)
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
    
    context = {
        'stana': text,
        'countries': countries,
        'cities': cities,
        'pubs': pubs,
        'form': ArticleForm,
    }
    
    return render(request, 'template_tags/templates_tags.html', context)

@transaction.atomic
def register_user(request):
    # import ipdb; ipdb.set_trace()

    if request.method == 'GET':
        context = {
            'profile_form': ProfileForm(),
            # 'user_form': RegisterForm(),
            'user_form': UserCreationForm(),
        }
    else:
        # user_form = RegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponse('Create User SUCCESS!'
                                '<br>'
                               f'<a href="/">Return to home page</a>'
            )

        context = {
            # 'user_form': RegisterForm(),
            'user_form': UserCreationForm(),
            'profile_form': ProfileForm(),
        }

    return render(request, 'register_user.html', context)


def login_user(request):
    # import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        context = {
            'login_form': LoginForm()
        }
        return render(request, 'login.html', context)
    else:
        login_form = LoginForm(request.POST)
        return_url = get_redirect_url(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(return_url)
        context = {
            'login_form': login_form
        }
        return render(request, 'login.html', context)
    # if request.user.is_authenticated:
    #     login(request, request.user)
    #     return redirect('home')
    # return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')