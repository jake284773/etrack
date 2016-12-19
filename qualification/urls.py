from django.conf.urls import url

from . import views

app_name = 'qualification'

urlpatterns = [
    url(r'^create$', views.QualificationCreate.as_view(), name='create'),
    # url(r'^(?P<pk>[0-9]+)/$', views.QualificationDetail.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/update$', views.QualificationUpdate.as_view(), name='update'),
    # url(r'^(?P<pk>[0-9]+)/delete', views.QualificationDelete.as_view(), name='delete'),
    # url(r'^$', views.QualificationList.as_view(), name='list'),
]