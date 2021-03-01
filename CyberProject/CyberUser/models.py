from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from datetime import date

#********************CyberUser********************
from django.utils import timezone


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
    wallet = models.PositiveIntegerField(default=0)


#********************CyberMain********************
class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']


class Like(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Dislike(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


#********************CyberBet********************

class Team(models.Model):
    name = models.CharField(max_length=50)
    win_count = models.PositiveIntegerField(default=0)
    lose_count = models.PositiveIntegerField(default=0)
    tie_count = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=25)
    moral = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name

class TeamA(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class TeamB(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Match(models.Model):
    tital = models.CharField(max_length=100)
    status = (
        ('Starting soon', 'Starting soon'),
        ('Live','Live'),
        ('Finished', 'Finished')
    )
    win_tie_lose = (
        ('TeamA Win', 'TeamA Win'),
        ('TeamB Win', 'TeamB Win'),
        ('Tie', 'Tie')
    )
    teamA = models.ForeignKey(TeamA, on_delete=models.CASCADE)
    teamB = models.ForeignKey(TeamB, on_delete=models.CASCADE)
    match_status = models.CharField(choices=status, max_length=50)
    match_result = models.CharField(choices=win_tie_lose, max_length=50, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.teamA} {self.teamB}"

    class Meta:
        ordering = ['-published_date']

class Bet(models.Model):
    win_tie_lose = (
        ('TeamA Win', 'TeamA Win'),
        ('TeamB Win', 'TeamB Win'),
        ('Tie', 'Tie')
    )
    status = (
        ('Starting soon', 'Starting soon'),
        ('Live', 'Live'),
        ('Finished', 'Finished')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    match_res = models.CharField(choices=win_tie_lose, max_length=50)
    money = models.PositiveIntegerField(default=0)












