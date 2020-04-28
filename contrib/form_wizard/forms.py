from django import forms

class ContactFormStepOne(forms.Form):
    first_name = forms.CharField(label='Име', max_length=50)
    last_name = forms.CharField(label='Фамилия', max_length=50)
    eng = forms.CharField(label='ЕГН', max_length=10)


class ContactFormStepTwo(forms.Form):
    phone = forms.CharField(label='Мобилен телефон', max_length=10)
    email = forms.EmailField(label='E-mail',max_length=150)