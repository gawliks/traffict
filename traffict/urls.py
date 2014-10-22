from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'traffict.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^api_manager/', include('api_manager.urls', namespace='api_manager')),
    url(r'^traffic_runner/', include('traffic_runner.urls', namespace='traffic_runner')),
    url(r'^admin/', include(admin.site.urls)),
)
