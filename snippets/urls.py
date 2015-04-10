from django.conf.urls import patterns, url
from snippets import views

urlpatterns = patterns('',
    url(r'^$', views.snippet_list, name="list"),
    url(r'^(?P<snippet_pk>\d+)', views.snippet_detail, name='detail'),
    url(r'^new/', views.snippet_new, name="new"),
)
