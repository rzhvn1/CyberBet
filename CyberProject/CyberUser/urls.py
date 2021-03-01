from django.urls import path
from .views import *

urlpatterns = [
    path('', news_page, name ='news-page'),
    path('news/<int:news_id>/', news_detail_page, name = 'news-detail-page'),
    path('like/<int:news_id>/', like, name = 'like'),
    path('dislike/<int:news_id>/', dislike, name = 'dislike'),
    path('signup/', signup_page, name = 'signup-page'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_email_page, name = 'activate-email-page'),
    path('login/', login_page, name = 'login-page'),
    path('profile/', profile_page, name = 'profile-page'),
    path('match/', match_page, name ='match-page'),
    path('match/<int:match_id>/', match_detail_page, name = 'match-detail-page'),
    path('update_match/<int:match_id>/', update_match_page, name = 'update-match-page'),


]