from django import forms
from django.contrib.auth.forms import UserCreationForm

from .BootstrapFormMixin import BootstrapFormMixin
from .models import UsersProfile


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settup_form()

class UsersProfileForm(forms.ModelForm, BootstrapFormMixin):
    class Meta:
        model = UsersProfile
        fields = ('profile_picture',)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settup_form()