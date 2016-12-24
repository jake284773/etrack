from django.conf.urls import url, include

from . import views

app_name = 'qualification'

pathway_urls = ([
    url(r'^create$', views.PathwayCreate.as_view(), name='create'),
], 'pathway')

unit_urls = ([
    url(r'^create$', views.UnitCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.UnitDetail.as_view(), name='detail'),
    url(r'^$', views.UnitList.as_view(), name='list'),
], 'unit')

urlpatterns = [
    url(r'^create$', views.QualificationCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.QualificationDetail.as_view(),
        name='detail'),
    # url(r'^(?P<pk>[0-9]+)/update$', views.QualificationUpdate.as_view(),
    #     name='update'),
    # url(r'^(?P<pk>[0-9]+)/delete', views.QualificationDelete.as_view(),
    #     name='delete'),
    url(r'^$', views.QualificationList.as_view(), name='list'),

    url(r'^(?P<qualification_id>[0-9]+)/pathways/', include(pathway_urls)),
    url(r'^units/', include(unit_urls)),
]
