from django.shortcuts import render
from django.contrib.auth import signals
from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse_lazy

from axes.decorators import axes_dispatch

from .forms import LoginForm
from django.contrib.auth import authenticate, login


@method_decorator(axes_dispatch, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
    """
    Custom login view that takes JSON credentials
    """

    http_method_names = ['post']

    def post(self, request):
        form = LoginForm(request.POST)

        if not form.is_valid():
            # inform django-axes of failed login
            signals.user_login_failed.send(
                sender=User,
                request=request,
                credentials={
                    'username': form.cleaned_data.get('username'),
                },
            )
            return HttpResponse(status=400)

        user = authenticate(
            request=request,
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
        )

        if user is not None:
            login(request, user)

            signals.user_logged_in.send(
                sender=User,
                request=request,
                user=user,
            )

            return JsonResponse({
                'message':'success'
            }, status=200)

        # inform django-axes of failed login
        signals.user_login_failed.send(
            sender=User,
            request=request,
            credentials={
                'username': form.cleaned_data.get('username'),
            },
        )

        return HttpResponse(status=403)


# def locked_out(request):
#     if request.POST:
#         form = AxesCaptchaForm(request.POST)
#         if form.is_valid():
#             ip = get_ip_address_from_request(request)
#             reset(ip=ip)
#             return HttpResponseRedirect(reverse_lazy('signin'))
#     else:
#         form = AxesCaptchaForm()

#     return render('captcha.html', dict(form=form), context_instance=RequestContext(request))
