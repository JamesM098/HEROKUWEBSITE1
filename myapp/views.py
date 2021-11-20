from django.shortcuts import render
from django.http import HttpResponse

def index(request, page=0):
  context ={
    "title":"Home",
    "display_requirement": "Login.png",

  }

  return render(request, "index.html", context=context) 