
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
]