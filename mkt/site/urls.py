from django.conf import settings
from django.conf.urls import patterns, url

import jingo

from . import views

def template_plus_xframe(request, template, **kwargs):
    r = jingo.render(request, template, kwargs)
    r['x-frame-options'] = 'allow-from ' + settings.BROWSERID_DOMAIN
    return r


urlpatterns = patterns('',
    url('^mozmarket.js$', views.mozmarket_js, name='site.mozmarket_js'),
    url('^privacy-policy$', template_plus_xframe,
        {'template': 'site/privacy-policy.html'}, name='site.privacy'),
    url('^terms-of-use$', template_plus_xframe,
        {'template': 'site/terms-of-use.html'}, name='site.terms'),
    url('^robots.txt$', views.robots, name='robots.txt'),
    url('^manifest.webapp$', views.manifest, name='manifest.webapp'),
    url('^csrf$', views.csrf, name='csrf'),
    url('^timing/record$', views.record, name='mkt.timing.record'),
)
