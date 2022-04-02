from django.urls import path, include
from rest_framework import routers

from internet_banking.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),

]