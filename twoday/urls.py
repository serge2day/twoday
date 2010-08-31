from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^twoday/', include('twoday.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^grappelli/', include('grappelli.urls')),
    
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/django_projects/workspace/platform/media/'}),
    
    (r'^media/admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/django_projects/workspace/platform/media/admin/media/'}),


)
