from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
url(r'^$', 'core.views.home', name='home'),
(r'^admin/', include(admin.site.urls))
)