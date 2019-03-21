from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Это первое представление")

def note(request):
    return HttpResponse("второе представление")
