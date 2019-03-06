from django.contrib import admin

# Register your models here.
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name' , 'beds_number' , 'weekday_price' , 'weekend_price']

admin.site.register(Room, RoomAdmin)
