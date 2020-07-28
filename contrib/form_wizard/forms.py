from django import forms
from captcha.fields import CaptchaField

from .models import Client


class ContactFormStepOne(forms.Form):
    first_name = forms.CharField(label='Име', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    eng = forms.CharField(label='ЕГН', max_length=10)


class ContactFormStepTwo(forms.Form):
    phone = forms.CharField(label='Мобилен телефон', max_length=10)
    email = forms.EmailField(label='E-mail',max_length=150)


class ContactFormStepTree(forms.Form):
    nickname = forms.CharField(label='Име', max_length=50)
    password_first = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_again = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()

        p1 = cleaned_data.get('password_first')
        p2 = cleaned_data.get('password_again')

        if p1 != p2:
            raise forms.ValidationError("You password don't match")
        return cleaned_data


# create a form 
class Formset(forms.Form): 
    title = forms.CharField() 
    description = forms.CharField() 


class FormMessages(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'eng', 'phone', 'email', )

    def __init__(self, *args, **kwargs):
        super(FormMessages, self).__init__(*args, **kwargs)
        self.fields['first_name'].help_text = '<br/>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.<br/>'
