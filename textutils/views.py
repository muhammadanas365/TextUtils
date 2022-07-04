# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("new line")

def spaceremove(request):
    return HttpResponse("space remover")


def charcount(request):
    return HttpResponse("charcount")


