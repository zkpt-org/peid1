from django.conf.urls import patterns, url
from intervention import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)