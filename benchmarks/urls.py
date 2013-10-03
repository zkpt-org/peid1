from django.conf.urls import patterns, url
from benchmarks import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)