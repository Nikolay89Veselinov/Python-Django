import json

from django.http import HttpResponse

from django.core import serializers

from django.shortcuts import render

from .models import Country, City, Pub


def filter(request):
    countries = Country.objects.all()
    cities = City.objects.all()
    pubs = Pub.objects.filter(active=True)
    data = {}

    for city in cities:
        data.setdefault(city.country.id, []).append({
            'id': city.id,
            'city': city.name,
        })

    context = {
        'data': json.dumps(data),
        'countries': countries,
        'cities': cities,
        'pubs': pubs,
    }

    return render(request, 'filter.html', context)


def get_country(request):
    country_id = request.GET.get('country_id')
    data = []
    if country_id != 'empty':
        cities = City.objects.filter(country__pk=country_id)

        for city in cities:
            data.append({
                'id': city.id,
                'city': city.name,
            })

    json_content = json.dumps(data).encode('utf-8')

    return HttpResponse(json_content, 'application/json; charset=utf-8')


def get_pub(request):
    get_pub = request.GET.get('pub_id')
    data = []
    if get_pub != 'empty':
        pubs = Pub.objects.filter(city__pk=get_pub, active=True)

        for pub in pubs:
            data.append({
                'id': pub.pk,
                'pub': pub.name
            })

    json_content = json.dumps(data).encode('utf-8')

    return HttpResponse(json_content, 'applications/json; charset=utf-8')