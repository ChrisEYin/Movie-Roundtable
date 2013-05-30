from django.conf.urls import patterns, include, url
from django.conf import settings
from qanda.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('qanda.urls')),
	url(r'^home/', include('qanda.urls')),
	url(r'^accounts/', include('qanda.urls')),
	url(r'^admin/', include(admin.site.urls)),
)