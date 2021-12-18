from django import forms
from django.forms import ModelForm
from .models import HikeModel
from .models import Locations


class HikeForm(ModelForm):
 class Meta:
  model = HikeModel
  fields = ('hike_name', 'hike_location', 'hike_description', 'hike_difficulty')


class LocationForm(ModelForm):
 class Meta:
  model = Locations
  fields = ('location_name','location_description')
