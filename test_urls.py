from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

admin.autodiscover()

urlpatterns = [
    re_path(r'^invitations/', include('invitations.urls')),
    re_path(r'^admin/', admin.site.urls),
]

if 'allauth' in settings.INSTALLED_APPS:
    urlpatterns.append(
        re_path(r'^accounts/', include('allauth.urls'))
    )
