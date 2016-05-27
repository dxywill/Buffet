from django.conf.urls import patterns, url
from shing import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))

