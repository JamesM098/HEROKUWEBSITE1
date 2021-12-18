from django.db import models

# Create your models here.


class Locations(models.Model):
 location_name = models.CharField('Location Name', max_length=50)
 location_description = models.CharField(max_length=200, blank=True)
 def __str__(self):
    return self.location_name


class HikeMeUsers(models.Model):
 first_name = models.CharField(max_length = 30)
 last_name = models.CharField(max_length = 30)
 email = models.EmailField('User Email')
 def __str__(self):
     return self.first_name + ' ' + self.last_name

class HikeModel(models.Model):
 hike_name = models.CharField(max_length=50)
 hike_description = models.TextField(max_length=200, blank=True)
 hike_location = models.ForeignKey(Locations, blank=True, null=True, on_delete=models.CASCADE)
 hike_difficulty = models.CharField(default="hard",max_length=50, blank=True)
 hike_hikers = models.ManyToManyField(HikeMeUsers, blank = True)
 def __str__(self):
     return self.hike_name



