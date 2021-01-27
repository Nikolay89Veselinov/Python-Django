from django import forms
from django.urls.conf import include

from .models import Comment, Pet


class CommenForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control rounded-2',    
            }
        )
    )

class CommenViewsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Pet
        exclude = ('user',)