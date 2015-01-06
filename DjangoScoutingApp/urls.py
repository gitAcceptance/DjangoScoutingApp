from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoScoutingApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scoutingData/', include('scoutingData.urls', namespace="scoutingData")),
    url(r'^admin/', include(admin.site.urls)),
)
