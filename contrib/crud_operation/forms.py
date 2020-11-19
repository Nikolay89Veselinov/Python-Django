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
