from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(label='Your name', max_length=20)
    password = forms.CharField(label='Your password', max_length=20)


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='E-Mail', max_length=30)
    # first_name = forms.CharField(label='Your first name', max_length=20)
    # last_name = forms.CharField(label='Your last name', max_length=20)
