from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Test 1 - Love James")
# Create your views here.
