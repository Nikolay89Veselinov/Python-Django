from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from contrib.sort_filter.models import City

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