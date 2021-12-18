from django.contrib import admin

from .models import HikeModel
from .models import HikeMeUsers
from .models import Locations

# Register your models here.
admin.site.register(Locations)
#admin.site.register(HikeModel)
admin.site.register(HikeMeUsers)


@admin.register(HikeModel)
class HikeModelAdmin(admin.ModelAdmin):
 list_display = ('hike_name', 'hike_location')
 ordering = ('hike_name',)
 search_fields = ('hike_name','hike_location__location_name')

