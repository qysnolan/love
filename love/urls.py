from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

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
]
