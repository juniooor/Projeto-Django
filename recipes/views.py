from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello world')
# Create your views here.


def contato(request):
    return HttpResponse('Contato')


def sobre(request):
    return HttpResponse('Sobre')
