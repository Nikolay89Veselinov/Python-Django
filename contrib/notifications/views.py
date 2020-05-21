import json

from django.shortcuts import render

from django.http import HttpResponse
from django.core import serializers

from .models import Notification



def get_notification(request):
    notifications = Notification.objects.filter(active=True)
    data = {'render_template': None}
    context = {
        'message' : []
        }
    request.session.setdefault('show_message', [])

    for notification in notifications:
        context['message'].append(notification.message)
        render_template = render(request, 'popup.html', context)
        data = {
            'render_template': render_template.content.decode("utf-8"),
        }
        json_content = json.dumps(
            data
        ).encode('utf-8')

    return HttpResponse(json_content, 'application/json; charset=utf-8')