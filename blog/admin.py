from django.contrib import admin
from blog.models import Blog, Author, Entry # наша модель из blog/models.py



admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
