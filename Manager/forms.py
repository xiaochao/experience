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
    password = forms.CharField(max_length=60, widget=forms.PasswordInput())


class BugContentForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(max_length=1000)
    sign = forms.CharField(max_length=10)

class CommentForm(forms.Form):
    vomit = forms.CharField(max_length=500)

class PersonalForm(forms.Form):
    gender = forms.BooleanField()
    industry = forms.CharField(max_length=200)
    skill = forms.CharField(max_length=100)
    introduce = forms.CharField(max_length=200)
