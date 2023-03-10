from django.shortcuts import render
from django.views.generic.base import View, HttpResponse, HttpResponseRedirect
from .forms import LoginForm, SignUpForm, NewVideoForm, CommentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Video, Comment
import string
import random
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:10]
        print(most_recent_videos)
        return render(request, self.template_name, {'menu_active_item': 'home', 'most_recent_videos': most_recent_videos})


class VideoView(View):
    template_name = 'video.html'

    def get(self, request, id):

        # print(request)
        print('Video-ID: {}'.format(id))
        # print(dir(request))
        video_by_id = Video.objects.get(id=id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = BASE_DIR+'/'+video_by_id.path
        context = {'video': video_by_id}
        if request.user.is_authenticated == True:
            comments_form = CommentForm()
            context['form'] = comments_form
        return render(request, self.template_name)


class CommentView(View):
    template_name = 'comment.html'

    def post(self, request):
        form = CommentForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            video_id = request.POST['video']
            video = Video.objects.get(id=video_id)
            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            return HttpResponseRedirect('/video/{}'.format(str(video_id)))

        return HttpResponse('VideoComment View POST')


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('You are already logged in')
            print(request.user)
            # logout(request)
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
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/')
            # return HttpResponseRedirect('Logintest for upload')
        variableA = 'New Video'
        form = NewVideoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass the HTML-Form
        form = NewVideoForm(request.POST, request.FILES)

        print(form)
        # print(request.POST)
        # print(request.FILES)

        if form.is_valid():
            # create a new Video entry
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']

            random_char = ''.join(random.choices(
                string.ascii_uppercase + string.digits, k=10))
            path = random_char+file.name

            new_video = Video(
                title=title,
                description=description,
                user=request.user,
                path=path)
            new_video.save()
            # print(new_video)
            # todo: redirect to detailed view page of a video
            return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:

            return HttpResponse('Invalid video submission. Please retry at your convenience.')
