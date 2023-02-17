from django.shortcuts import render
from django.views.generic.base import View, HttpResponse


class Index(View):
    template_name = 'index.html'

    def get(self, request):
        variableA = 'Index'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variableA': variableA})

    def post(self, request):
        return HttpResponse('This is Index view. POST Request')
