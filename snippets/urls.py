from django.conf.urls import patterns, url
from snippets import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CityBuzz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.snippet_list, name="list"),
    url(r'^(?P<snippet_pk>\d+)', views.snippet_detail, name='detail'),
)
