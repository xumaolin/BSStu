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

                       url(r'^manage_login$', 'student.views.manage_login', name='manage_login'),
                       url(r'^manage$', 'student.views.student_manage', name='student_manage'),
                       url(r'^add_student$', 'student.views.add_student', name='add_student'),
                       url(r'^student_update$', 'student.views.student_update', name='student_update'),
                       url(r'^edit_profile$', 'student.views.edit_profile', name='edit_profile'),
                       url(r'^delete$', 'student.views.delete_student', name='delete_student'),

                       url(r'^$', 'student.views.index'),
                       url(r'^login$', 'student.views.user_login', name='user_login'),
                       url(r'^dashboard$', 'student.views.dashboard', name='dashboard'),
                       url(r'^update_info$', 'student.views.update_info', name='update_info'),
                       )
