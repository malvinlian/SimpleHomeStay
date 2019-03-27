from django.db import models
from django.conf import settings
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

    CheckIn = models.DateField()
    CheckOut = models.DateField()

    nights = models.PositiveIntegerField(default = 0)

    TotalCost = models.PositiveIntegerField(default = 0,null=True)
    notes  = models.TextField()


    class Meta:
        verbose_name_plural = 'Reservation'

    def __str__(self):
      return "%s" %(self.room)
