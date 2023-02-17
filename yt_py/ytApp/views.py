from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm, SignUpForm


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'variableA': variableA})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('HELLO LOGIN')
        return HttpResponse('This is Login view. POST Request')


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('HELLO SignUp')
        return HttpResponse('This is SignUp view. POST Request')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        form = FormClass()
        return render(request, self.template_name, {'variableA': variableA, 'from': form})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request')
