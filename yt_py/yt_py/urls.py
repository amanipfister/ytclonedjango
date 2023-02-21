from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from ytApp.views import HomeView, NewVideo, LoginView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('login', LoginView.as_view()),
    path('signup', SignUpView.as_view())
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns
