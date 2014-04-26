from django.conf.urls import patterns, url
from cyclecellgrid import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^cyclecell', views.cyclecell, name='cyclecell')
)
