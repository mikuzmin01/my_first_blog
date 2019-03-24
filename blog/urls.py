from django.conf.urls import url
from . import views

from blog.views import PostsListView, PostDetailView

from django.contrib import admin


admin.autodiscover()  #функция автоматического обнаружения файлов admin.py
# в приложениях

app_name = 'blog'


urlpatterns = [
    url(r'^start', views.index, name='index'),
    url(r'^$', PostsListView.as_view(), name='list'),
    # то есть по URL http://имя_сайта/blog/
    # будет выводиться список постов
    url(r'^note', views.note, name='note'),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    # а по URL http://имя_сайта/blog/число/
    # будет выводиться пост с определенным номером
]