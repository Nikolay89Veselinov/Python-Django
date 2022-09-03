from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import ASD

monthly_chalenges = {
    "january": "Eat no meat",
    "february": "Walk for at least 20 minutes every day",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat",
    "may": "Walk for at least 20 minutes every day",
    "june": "Workout",
    "July": "Learn Django for at least 20 minutes every day!",
    "august": "Eat no meat",
    "september": "Learn English",
    "octomber": "Walk for at least 20 minutes every day",
    "novenber": "Learn Django for at least 20 minutes every day!",
    "december": "Workout"
}


def monthly_challenge(request, month):

    try:
        callenge_text = monthly_chalenges[month]
        return HttpResponse(callenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge_by_numbers(request, month):
    months = list(monthly_chalenges.keys())

    if month > len(months):

        return HttpResponseNotFound('Invalid month!')

    redirecr_month = months[month - 1]
    reverse_url = reverse('challenge:month-challenge', args=[redirecr_month])
    return HttpResponseRedirect(reverse_url)
    # return HttpResponseRedirect('/challenge/' + redirecr_month)