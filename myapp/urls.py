from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from  django.urls import re_path

urlpatterns = [
  path('', views.index),
  path('log-in-page/', views.login),
  path('welcome', views.welcome),
  path('hikes/', views.hikes, name = 'hikes_url'),
  path('hikes/all-hikes/', views.all_hikes, name = "all-hikes"),
  path('live-chat/', views.live_chat),
  path('about/', views.about),
  path('help/', views.help),
  path('admin/', admin.site.urls),
  path('show_hike/<hike_id>', views.show_hikes, name = "show-hike"),
  path('add_hike', views.add_hike, name = "add-hike"),
  path('add_location', views.add_location, name = "add-location"),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]