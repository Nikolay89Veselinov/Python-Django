from django import forms
from django.forms import widgets

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'active', )

        widgets = {
            'title': forms.Textarea(
                attrs={
                    'class': 'my-textarea '
                },
            ),
        }
        