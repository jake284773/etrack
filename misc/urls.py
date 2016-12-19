from django.conf.urls import url, include

from . import views

app_name = 'misc'

subjectsector_patterns = ([
    url(r'^create$', views.SubjectSectorCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.SubjectSectorDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update$', views.SubjectSectorUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete', views.SubjectSectorDelete.as_view(), name='delete'),
    url(r'^$', views.SubjectSectorList.as_view(), name='list'),
], 'subject-sector')

faculty_patterns = ([
    url(r'^create$', views.SubjectSectorCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.SubjectSectorDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update$', views.SubjectSectorUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete', views.SubjectSectorDelete.as_view(), name='delete'),
    url(r'^$', views.SubjectSectorList.as_view(), name='list'),
], 'faculty')

urlpatterns = [
    url(r'^subject-sector/', include(subjectsector_patterns)),
    url(r'^faculty/', include(faculty_patterns)),
]
