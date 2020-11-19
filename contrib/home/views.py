from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from contrib.form_wizard.models import Client
from contrib.sort_filter.models import City, Country, Pub
from contrib.based_views.forms import ArticleForm

def home(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

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