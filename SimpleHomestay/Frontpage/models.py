from django.db import models

# Create your models here.
class Frontpage(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=12)
    office_number = models.CharField(max_length=12)
    message1 = models.TextField(null=False)
    check_in = models.CharField(max_length=12, null=True)
    check_out = models.CharField(max_length=12, null=True)
    promotion = models.TextField(null=True)

    image1 = models.ImageField(upload_to='home/' , null=True)
    gallery1 = models.ImageField(upload_to='home/' , null=True)
    gallery2 = models.ImageField(upload_to='home/' , null=True)
    gallery3 = models.ImageField(upload_to='home/' , null=True)
    gallery4 = models.ImageField(upload_to='home/' , null=True)
    gallery5 = models.ImageField(upload_to='home/' , null=True)
    gallery6 = models.ImageField(upload_to='home/' , null=True)
    promotion1 = models.ImageField(upload_to='home/' , null=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Frontpage'
        verbose_name_plural = 'Frontpage'
