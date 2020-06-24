
import requests
import json

from django.http import HttpResponse
from django.shortcuts import render


OPERATION = {
    'addition': '+',
    'subtraction': '-',
    'multiplication': '*',
    'division': '/',

}

def get_response(request):

    url = 'http://127.0.0.1:8003/'
    headers = {'content-type': 'application/json; charset=utf-8'}

    if request.is_ajax():
        data = {
        'x': request.GET.get('first_number'),
        'y': request.GET.get('second_number'),
        'operation': request.GET.get('operation')
        }

        if request.method == "GET":
            response = requests.get(url, params=data, headers=headers)
        elif request.method == "POST":
            response = requests.post(url, data=data, headers=headers)

        return HttpResponse(response, 'application/json; charset=utf-8')

    context = {
        'operations': OPERATION,
    }
    return render(request, 'calculator.html', context)
