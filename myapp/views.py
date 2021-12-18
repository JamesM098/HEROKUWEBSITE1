from django.shortcuts import render
from .models import HikeModel
from .models import HikeMeUsers

from django.http import HttpResponseRedirect
from .forms import HikeForm
from .forms import LocationForm





# Create your views here.



def add_location(request):
  submitted = False
  form = LocationForm
  if request.method == "POST":
    form = LocationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/add_hike')
    else:
      form = LocationForm
      if 'submitted' in request.GET:
        submitted = True
  return render(request, "add_location.html",{'title':'Add a Location...','form':form, 'submitted':submitted}) 


def add_hike(request):
  submitted = False
  form = HikeForm
  if request.method == "POST":
    form = HikeForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/hikes/all-hikes')
    else:
      form = HikeForm
      if 'submitted' in request.GET:
        submitted = True
  return render(request, "add_hike.html",{'title':'Add a Hike...','form':form, 'submitted':submitted}) 



def show_hikes(request, hike_id):
  hike = HikeModel.objects.get(pk=hike_id)
  return render(request, "show_hike.html",{'hike':hike}) 

def index(request, page=0):
  context ={
    "title":"Home",
    "display_requirement": "Login.png",

  }

  return render(request, "index.html", context=context) 

def login(request):
  context={
    "title":"Logging In..."
  }
  return render(request, "login.html", context = context)

def welcome(request):
  context={
    "title":"Welcome!"
  }
  return render(request, "welcome.html", context = context)


def hikes(request):
  context = {"title":"Hikes"}
  if request.method == "POST":
    searched = request.POST['searched']
    name_search = HikeModel.objects.filter(hike_name__contains=searched)
    location_search = HikeModel.objects.filter(hike_location__location_name__contains=searched)


    return render(request, 'hikes.html', {'title':"Hikes",'searched':searched, 'name_search':name_search, 'location_search':location_search})
  else:
    return render(request, "hikes.html", context)






def all_hikes(request):
  hike_list = HikeModel.objects.all()
  context={

    "title":"All Hikes",
    "hike_list":hike_list
  }

  return render(request, "all_hikes.html", context)







def live_chat(request):
  context={
    "title":"Live Chat"
  }
  return render(request, "live_chat.html", context = context)


def about(request):
  list_length = len(HikeModel.objects.all())
  user_length = len(HikeMeUsers.objects.all())
  context={
    "title":"About",
    "hike_count":list_length,
    "user_count":user_length,
  }
  return render(request, "about.html", context = context)


def help(request):
  context={
    "title":"HELP ME PLEASE"
  }
  return render(request, "help.html", context = context)