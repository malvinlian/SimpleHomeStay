from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin
from .models import Room,Reservation, Schedule
import datetime
import calendar
from django.urls import reverse
from django.utils.safestring import mark_safe


class RoomAdmin(admin.ModelAdmin):
    list_display = ['name' ,'bed_type', 'beds_number' , 'capacity'  , 'price']

admin.site.register(Room, RoomAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['room','name' ,'email' , 'CheckIn'  , 'CheckOut','nights','TotalCost','notes']

admin.site.register(Reservation, ReservationAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['summary','date' ,'start_time',]

admin.site.register(Schedule,ScheduleAdmin)
