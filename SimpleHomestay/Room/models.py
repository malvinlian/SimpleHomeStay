from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    bed_type = models.CharField(max_length=50, default='SOME STRING')
    beds_number = models.PositiveIntegerField()
    capacity = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='room/' , null=True)
    price = models.PositiveIntegerField()
    promotion = models.TextField()
    facility = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Room'

class Reservation(models.Model):
    room = models.ForeignKey(Room,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)

    email = models.EmailField()
    phone_number = models.CharField(max_length=12)

    NumberOfGuest = models.PositiveIntegerField(default = 0)

    CheckIn = models.DateTimeField()
    CheckOut = models.DateTimeField()

    nights = models.PositiveIntegerField(default = 0)

    TotalCost = models.PositiveIntegerField(default = 0,null=True)
    notes  = models.TextField()


    class Meta:
        verbose_name_plural = 'Reservation'

    def __str__(self):
         return self.name



class Schedule(models.Model):
    """Schedule"""
    Room_no = (
        ("!","!"),
        ("@","@"),
        ("#","#"),
        ("$","$"),
    )
    summary = models.CharField( max_length=1, choices=Room_no)
    description = models.TextField('description', blank=True)
    start_time = models.TimeField('start_time', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('end_time', default=datetime.time(7, 0, 0))
    date = models.DateField('date')
    

    def __str__(self):
        return self.summary
