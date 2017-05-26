from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
]

admin.site.site_header = 'Django responsive admin demo'
