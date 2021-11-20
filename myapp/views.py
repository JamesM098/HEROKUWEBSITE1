from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("WHADDUP DAWG - Love James")
# Create your views here.
