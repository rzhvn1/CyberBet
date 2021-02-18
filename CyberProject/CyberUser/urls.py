from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name = 'main-page'),
    path('signup/', signup_page, name = 'signup-page'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_email_page, name = 'activate-email-page'),
    path('login/', login_page, name = 'login-page'),
    path('profile/', profile_page, name = 'profile-page'),
]