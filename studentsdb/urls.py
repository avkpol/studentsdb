from django.conf.urls import patterns, include, url
from django.contrib import admin
from students.views.students import StudentUpdateView
from students.views.students import StudentDeleteView
from students.views.students import StudentAddView
from students.views.groups import GroupDeleteView
from students.views.journal import JournalView
urlpatterns = patterns('',
    # Students urls
    url(r'^$', 'students.views.students.students_list', name='home'),
	url(r'^students/add/$',
		StudentAddView.as_view(),
		name='students_add'),
    # url(r'^students/add/$', 'students.views.students.students_add',
    #          name='students_add'),
	url(r'^students/(?P<pk>\d+)/edit/$',
		StudentUpdateView.as_view(),
		name='students_edit'),
	url(r'^students/(?P<pk>\d+)/delete/$',
		StudentDeleteView.as_view(),
		name= 'students_delete'),
    # url(r'^students/(?P<sid>\d+)/edit/$',
    #          'students.views.students.students_edit',
    #          name='students_edit'),
    # url(r'^students/(?P<sid>\d+)/delete/$',
    #          'students.views.students.students_delete',
    #          name='students_delete'),
    
    # Groups urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add',
         name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit',
         name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$',GroupDeleteView.as_view(),
         name='group_delete'),
         
         
    # Exam urls
    url(r'^studexam/$', 'students.views.studexam.exam_list', name='studexam'),
    url(r'^studexam/add/$', 'students.views.studexam.studexam_add',
         name='studexam_add'),
   url(r'^studexam/edit/$', 'students.views.studexam.studexam_edit',
        name='studexam_edit'),
#    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete',
#         name='groups_delete'),
#         
    url(r'^studexam/edit/$', 'students.views.studexam.studexam_edit',
         name='studexam_edit'),
#    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete',
#         name='groups_delete'),
   
    # Journal urls
    url(r'^journal/$', JournalView.as_view(), name='journal'),



 # Contact Admin Form
   
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin',
	     name='contact_admin'),   
         
         
         
    url(r'^admin/', include(admin.site.urls)),
	
)


#add media files via DEBUG only while development,on production should make it directly via main server(e.g.Apache)
from .settings import MEDIA_ROOT,DEBUG



if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT}))
