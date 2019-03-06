from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    bed_type = models.CharField(max_length=50, default='SOME STRING')
    beds_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='room/' , null=True)
    weekday_price = models.PositiveIntegerField()
    weekend_price = models.PositiveIntegerField()
    promotion = models.TextField()
    facility = models.TextField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Room'
