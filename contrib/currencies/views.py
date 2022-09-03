from django.shortcuts import render
from .models import Currency
from datetime import datetime
from django.http import JsonResponse
from .models import Currency
import decimal


def exchange_rate(request):
    currency = Currency.objects.all()
    time = datetime.now()
    context = {
        'Currency': currency,
        'time': time
    }
    return render(request, 'currency_form.html', context)


def convert_currencies(request):
    if request.is_ajax():
        currency_from = Currency.objects.get(pk=request.POST.get('currency_from'))
        currency_to = Currency.objects.get(pk=request.POST.get('currency_to'))
        currency_value = request.POST.get("currency_value")
        result = decimal.Decimal(float(currency_value)) * (currency_from.course / currency_to.course)
        result = "{0:.{1}f}".format(result, 2)
        data = {
            "result": result,
        }
        return JsonResponse(data)
