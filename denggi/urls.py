from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'denggi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^harian/', include('harian.urls')),
	url(r'^negeri/', include('negeri.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
