from django import forms

from .models import ValidatorModel


class ValidatorModelForm(forms.ModelForm):
    class Meta:
        model = ValidatorModel
        fields = '__all__'
