from django.shortcuts import render

from formtools.wizard.views import SessionWizardView

from .models import Client
from .forms import ContactFormStepOne, ContactFormStepTwo, ContactFormStepTree


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