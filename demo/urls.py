from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^doc/', include('django.contrib.admindocs.urls')),
    url(r'^', admin.site.urls),
]

admin.site.site_header = 'Django responsive admin demo'
