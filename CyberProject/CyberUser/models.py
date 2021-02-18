from django.db import models
from django.contrib.auth.models import User
from datetime import date

#********************CyberUser********************
class Profile(models.Model):
    genders = (
        ('F', 'F'),
        ('M', 'M'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default-profile-image', blank=True)
    full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=255)
    gender = models.CharField(choices=genders, max_length=20)
    description = models.CharField(max_length=50)
    birth_day = models.DateField(default=date.today())
    wallet = models.PositiveIntegerField(default=0)





