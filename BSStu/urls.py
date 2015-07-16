from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BSStu.views.home', name='home'),
    # url(r'^BSStu/', include('BSStu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'student.views.index'),
    url(r'^login$', 'student.views.user_login', name='user_login'),
    url(r'^dashboard$', 'student.views.dashboard', name='dashboard'),
    url(r'^update_info$', 'student.views.update_info', name='update_info'),
)
