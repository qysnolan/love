from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls import patterns
from .views import *

handler401 = 'love.views.error_401'
handler403 = 'love.views.error_403'
handler404 = 'love.views.error_404'
handler500 = 'love.views.error_500'
handler502 = 'love.views.error_502'
handler504 = 'love.views.error_504'

urlpatterns = [
    # Examples:
    # url(r'^$', 'love.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RedirectView.as_view(pattern_name='love.views.home')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', 'love.views.home', name='home'),
    url(r'^wedding/', 'wedding.views.home', name='wedding'),
    url(r'^photo/', 'photo.views.home', name='photo'),
    url(r'^menu/', 'menu.views.home', name='menu'),

    # REST framework
    url(r"^api/", include("api.urls"), name="api_base"),

    # Error pages
    url(r'^401/$', error_401, name="error_401"),
    url(r'^403/$', error_403, name="error_403"),
    url(r'^404/$', error_404, name="error_404"),
    url(r'^500/$', error_500, name="error_500"),
    url(r"^502/$", error_502, name="error_502"),
    url(r"^504/$", error_504, name="error_504"),
    url(r"^maintenance/$", maintenance, name="maintenance"),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('', (r'^media/(?P<path>.*)$',
                                 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}))