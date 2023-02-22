from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, NewVideoForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'variableA': variableA})


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('You are already logged in')
            print(request.user)
            logout(request)
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out html-form from view to loginform()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # maybe add entry to logs with timestamp and ip later
                login(request, user)
                print('successful login')
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
        # return HttpResponse('This is Login view. POST Request')


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('You are already logged in')
            print(request.user)
            return HttpResponseRedirect('/')
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out html-form from view to signupform()
        form = SignUpForm(request.POST)
        if form.is_valid():
            # create a user account
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            # check_username = User.objects.get(username=username)
            # if check_username is not None:
            #     return 'Please provide a valid username'
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            # check_email = User.objects.get(email=email)
            # if check_email is not None:
            #     return 'Please provide a valid email'
            # return False
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            # print(new_user)
            new_user.save()
            # print(new_user)
            return HttpResponseRedirect('/login')
        return HttpResponse('This is SignUp view. POST Request')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        form = NewVideoForm()
        return render(request, self.template_name, {'variableA': variableA, 'form': form})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request')
