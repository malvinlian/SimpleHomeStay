from django.contrib import admin

# Register your models here.
from .models import Room,Reservation

class RoomAdmin(admin.ModelAdmin):
    list_display = ['name' ,'bed_type', 'beds_number' , 'capacity'  , 'price']

admin.site.register(Room, RoomAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['room','name' ,'email' , 'CheckIn'  , 'CheckOut' ]

admin.site.register(Reservation, ReservationAdmin)
