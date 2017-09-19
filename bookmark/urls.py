from django.conf.urls import url
from django.contrib import admin

from bookmark.models import Bookmark


from django.views.generic import ListView, DetailView

from .views import *

urlpatterns = [
    url(r'^$', ListView.as_view(model=Bookmark), name = 'index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail')
]