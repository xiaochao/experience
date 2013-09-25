from django import forms
from Manager.error import *


class RegisteForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())
    repassword = forms.CharField(max_length=60, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(RegisteForm, self).clean()
        pwd = cleaned_data.get('password')
        pwd2 = cleaned_data.get('repassword')
        eml = cleaned_data.get('email')

        if pwd != pwd2:
            self._errors['password'] = PASSWORD_NOT_SAME
        if not eml:
            self._errors['email'] = EMAIL_FORMAT_ERROR

        return cleaned_data

class LoginForm(forms.Form):
    name = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)


