from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=20)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='E-Mail', max_length=30)
    # first_name = forms.CharField(label='Your first name', max_length=20)
    # last_name = forms.CharField(label='Your last name', max_length=20)


class CommentForm(forms.Form):
    # username = forms.CharField(label='Username', max_length=20)
    text = forms.CharField(widget=forms.Textarea, label='Text', max_length=200)
    video = forms.HiddenInput()


class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=200)
    file = forms.FileField()
