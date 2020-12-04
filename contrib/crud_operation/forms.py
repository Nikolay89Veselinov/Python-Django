from django import forms
from django.forms.widgets import HiddenInput

from .models import News

class DisableFormMixin():
    def __init__(self):

        for _, field in self.fields.items():
            field.widget = HiddenInput()
            field.widget.attrs['delete'] = True


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'


# class InstanceForm(NewsForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         for _, field in self.fields.items():
#             # field.widget = HiddenInput()
#             field.widget.attrs['delete'] = True

class InstanceForm(NewsForm, DisableFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisableFormMixin.__init__(self)


class FilterForm(forms.Form):
    ORDER_ASC = 'asc'
    ORDER_DESC = 'desc'

    ORDER_CHOICES = (
        (ORDER_ASC, 'Ascendint'),
        (ORDER_DESC, 'Descending'),
    )

    text = forms.CharField(required=False)
    order = forms.ChoiceField(choices=ORDER_CHOICES, required=False)