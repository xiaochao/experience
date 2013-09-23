from django import forms


class RegisteForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=60)
    repassword = forms.CharField(max_length=60)

class LoginForm(forms.Form):
    name = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60)