# from captcha.fields import CaptchaField
from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128, required=True)


class AxesLoginForm(LoginForm):

    class Meta:
        model = LoginForm
        fields = ['username', 'password']

    def user_credentials(self):
        credentials = super().user_credentials()
        credentials['login'] = credentials.get('email') or credentials.get('username')
        return credentials





# class AxesCaptchaForm(forms.Form):
#     myfield = AnyOtherField()
#     captcha = CaptchaField()
