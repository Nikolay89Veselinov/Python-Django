from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits >= 5:
        del(request.session['num_visits'])
    context = {
        'view_count': ('view count ' + str(num_visits))
    } 
    return render(request, 'home.html', context)
