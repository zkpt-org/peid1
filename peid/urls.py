from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from peid import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'peid.views.home', name='home'),
    # url(r'^peid/', include('peid.foo.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', include('home.urls')),
    url(r'^outlook/', include('outlook.urls')),
    url(r'^outcomes/', include('outcomes.urls')),
    url(r'^intervention/', include('intervention.urls')),
    url(r'^benchmarks/', include('benchmarks.urls')),
)
urlpatterns += staticfiles_urlpatterns()