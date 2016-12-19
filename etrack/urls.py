import os

from django.conf.urls import url, include

urlpatterns = [
    url(r'^misc/', include('misc.urls')),
    url(r'^qualification/', include('qualification.urls')),
]

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'etrack.settings.dev':
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
