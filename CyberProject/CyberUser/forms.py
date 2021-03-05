from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Comment, Bet, Match


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user',]

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'


class BetForm(forms.ModelForm):
    class Meta:
        model = Bet
        fields = '__all__'
        exclude = ['rateA', 'rateB',]

class UpdateMatch(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['match_status',]
