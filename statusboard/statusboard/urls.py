from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    # url(r'^$', 'statusboard.views.home', name='home'),
    # url(r'^statusboard/', include('statusboard.foo.urls')),

    # admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
