from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)

