from django.http import JsonResponse
from django.shortcuts import render
from django.forms import formset_factory
from django.contrib import messages

from formtools.wizard.views import SessionWizardView

from .models import Client
from .forms import ContactFormStepOne, ContactFormStepTwo, ContactFormStepTree,\
                    Formset, FormMessages, WidgetForm


class ContactWizard(SessionWizardView):
    form_list = [ContactFormStepOne, ContactFormStepTwo, ContactFormStepTree]

    def done(self, form_list, form_dict, **kwargs):
        all_cleaned_data = self.get_all_cleaned_data()
        instance = Client(
            first_name = all_cleaned_data['first_name'],
            last_name = all_cleaned_data['last_name'],
            eng = all_cleaned_data['eng'],
            phone = all_cleaned_data['phone'],
            email = all_cleaned_data['email']
        )
        instance.save()

        if form_list:
            return render(self.request, 'formtools/wizard/done.html', {
                'form_data': [form.cleaned_data for form in form_list]
            })

  
def formset_view(request): 
    context ={} 
  
    # creating a formset 
    FormSet = formset_factory(Formset, extra=3, max_num=3) 
    formset = FormSet()
      
    # Add the formset to context dictionary 
    context['formset']= formset 
    return render(request, "formset.html", context)

def form_messages(request):
    # obj = Client.objects.get(id=60)

    if request.is_ajax():
        form = FormMessages(request.GET)
        captcha_error = True if 'captcha' in form.errors else False
        response = {
            "captcha_error": captcha_error,
        }
        return JsonResponse(response)

    if request.method == 'POST':
        form = FormMessages(request.POST, request.FILES)
        aa = form.errors['captcha']
        aa.clear()
        if 'captcha' in form.errors:
            del form.errors['captcha']
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
    else:
        # form = FormMessages(instance=obj)
        form = FormMessages()
    return render(request, 'form_message.html', {'form': form})


def widget_form(request):
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = WidgetForm()
    return render(request, 'widget_form.html', {'form': form})