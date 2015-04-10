from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('homepage.urls',namespace='homepage',app_name='homepage'), ),
    url(r'^snippets/', include('snippets.urls',namespace='snippets',app_name='snippets'), ),
)
