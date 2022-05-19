from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe



from .forms import OpenStreetMapsForm
from .models import OpenStreetMaps


def map(request):
    items = OpenStreetMaps.objects.all()
    json_items = [{
        'location': item.location,
        'location_lat': item.location_lat,
        'location_lon': item.location_lon
    } for item in items]
    if request.method == 'POST':
        form = OpenStreetMapsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success!')
    else:
        form = OpenStreetMapsForm()
        context = {
            'form': form,
            'object_json': mark_safe(DjangoJSONEncoder().encode(json_items)),

        }
        print(json_items, '11111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    return render(request, 'osm.html', context)
