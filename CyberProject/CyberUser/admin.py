from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Profile)
admin.site.register([News, Like, Dislike, Comment])
admin.site.register([Team, TeamA, TeamB, Match, Bet])