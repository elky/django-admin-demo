from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Django responsive admin demo'
