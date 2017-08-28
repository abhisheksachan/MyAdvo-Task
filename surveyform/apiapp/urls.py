from django.conf.urls import url, include
from django.conf import settings

from views import LoginForm, LogoutForm, AccountProfile, CreateForm, DisplayForm

urlpatterns = [

    url(r'^login', LoginForm.as_view()),
    url(r'^logout', LogoutForm.as_view()),
    url(r'^accounts/profile/', AccountProfile.as_view()),
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^form/create', CreateForm.as_view()),
    url(r'^form/display/(?P<formid>.+)', DisplayForm.as_view()),

]