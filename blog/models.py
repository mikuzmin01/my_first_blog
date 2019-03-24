from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=300) # заголовок поста
#     text = models.TextField(max_length=10000) # текст поста
#     created_date = models.DateTimeField(default=timezone.now)  #  default=timezone.now
#     published_date = models.DateTimeField(blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title

class Blog(models.Model):
    name = models.CharField(max_length=40, verbose_name='заголовок')
    tagline = models.CharField(max_length=300, verbose_name='подзаголовок')
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя')
    email = models.CharField(max_length=50, verbose_name='@email')

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(blank=True)
    mod_date = models.DateTimeField(default=timezone.now)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    n_comments = models.CharField(max_length=200)
    n_pingbacks = models.CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
