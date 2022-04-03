from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'internet_banking/index.html'

class AboutView(TemplateView):
    template_name = 'internet_banking/about.html'

class MyProfileView(TemplateView):
    template_name = 'internet_banking/my_profile.html'

def logout_user(request):
    logout(request)
    return redirect('home')


