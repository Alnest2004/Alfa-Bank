from django.urls import path, include
from rest_framework import routers

from internet_banking.views import HomePageView, AboutView, logout_user, MyProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about_us', AboutView.as_view(), name='about_us'),
    path('my_profile/<slug:url>/', MyProfileView.as_view(), name='my_profile'),

    path('logout', logout_user, name='logout'),
]