from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .forms import SignupForm
from .tokens import account_activation_token
from CyberProject.settings import EMAIL_HOST_USER
from .forms import *
from .models import News, Like, Dislike, Match, TeamA, TeamB, Bet




#********************CyberMain********************

def news_page(request):
    news = News.objects.all()
    context = {'news':news}
    return render(request, 'CyberUser/news_page.html', context)

def news_detail_page(request, news_id):
    news = News.objects.get(id=news_id)
    likes = news.like_set.all().count()
    dislikes = news.dislike_set.all().count()
    comments = news.comment_set.all()
    form = CommentForm(initial={'news':news, 'user':request.user})
    if request.method == 'POST':
        form = CommentForm(request.POST ,initial={'news':news, 'user':request.user})
        if form.is_valid():
            form.save()
    context = {'news':news, 'likes':likes, 'dislikes':dislikes, 'form':form, 'comments':comments }
    return render(request, 'CyberUser/news_detail_page.html', context)

def like(request, news_id):
    new, created = Like.objects.get_or_create(user=request.user, news_id = news_id)
    if not created:
        return HttpResponse('You already liked this')
    else:
        return redirect('news-page')

def dislike(request, news_id):
    new, created = Dislike.objects.get_or_create(user=request.user, news_id = news_id)
    if not created:
        return HttpResponse('You already disliked this')
    else:
        return redirect('news-page')


#********************CyberUser********************


def signup_page(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            Profile.objects.create(wallet=0, user = user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('user_dir/acc_active_email.html', context = {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')

            send_mail(subject=mail_subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=[to_email], html_message=message)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'CyberUser/signup_page.html', {'form': form})

def activate_email_page(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect('news-page')

    return render(request, 'CyberUser/login_page.html')

def profile_page(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form, 'user':user}
    return render(request, 'CyberUser/profile_page.html', context)

def match_page(request):
    matchs1 = Match.objects.filter(match_status='Starting soon')
    matchs2 = Match.objects.filter(match_status='Live')
    matchs3 = Match.objects.filter(match_status='Finished')
    context = {'matchs1':matchs1, 'match2':matchs2, 'match3':matchs3}
    return render(request, 'CyberUser/match_page.html', context)

def match_detail_page(request, match_id):
    match = Match.objects.get(id=match_id)
    form = BetForm(initial={'match':match, 'user':request.user})
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        form = BetForm(request.POST)
        if form.is_valid():
            form.save()
            profile.wallet -= form.cleaned_data['money']
            profile.save()
    context = {'match': match, 'form': form, 'wallet': request.user.profile.wallet}
    return render(request, 'CyberUser/match_detail_page.html', context)


def update_match_page(request, match_id):
    try:
        match = Match.objects.get(id = match_id)
        form = UpdateMatch(instance=match)
        bets = match.bet_set.all()
        betsA = match.bet_set.filter(match_res='TeamA Win').count()
        betsB = match.bet_set.filter(match_res='TeamB Win').count()
        rateA = 0
        rateB = 0
        if betsA > betsB:
            rateA = betsB // betsA
            rateB = betsA // betsB
        elif betsA < betsB:
            rateA = betsA // betsB
            rateB = betsB // betsA
        if request.method == 'POST':
            form = UpdateMatch(request.POST, instance=match)
            if form.is_valid():
                form.save()
                for bet in bets:
                    if bet.match_res == match.match_result:
                        print(match.match_result)
                        bet.user.profile.wallet += bet.money * rateA
                        bet.user.profile.save()
                    elif bet.match_res == match.match_result and match.match_result == 'TeamB Win':
                        bet.user.profile.wallet += bet.money * rateB
                        bet.user.profile.save()
                else:
                    return redirect('match-page')
        return render(request, 'CyberUser/update_match_page.html', {'form':form})
    except Match.DoesNotExist:
        return HttpResponse('Page Not Found!')












