from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    url(r'blog', views.index, name='index'),
    url(r'note', views.note, name='note')
]