from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Entry
from django.views.generic import ListView, DetailView

def index(request):
    return HttpResponse("Это первое представление")

def note(request):
    return HttpResponse("второе представление")


# def index(request):
#     return render(request, "partial/index.html")
#
#
# def single_note(request, id=None):
#     return render(request, "partial/single_note.html")



class PostsListView(ListView): # представление в виде списка
    model = Entry                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Entry