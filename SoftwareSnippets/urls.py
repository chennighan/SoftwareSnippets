from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.flatpages import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SoftwareSnippets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.flatpage, {'url': '/'}, name='index'),
    url(r'^snippets/', include('snippets.urls',namespace='snippets',app_name='snippets'), ),
)
