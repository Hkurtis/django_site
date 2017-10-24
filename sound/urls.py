from django.conf.urls import url
from . import views

urlpatterns=[
    #basic Sound pattern
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    #/shows/69
    url(r'^(?P<show_num>[0-9]+)/$', views.detail, name='detail'),
]
