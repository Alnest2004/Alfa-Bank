from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView

from users.models import User


class HomePageView(TemplateView):
    template_name = 'internet_banking/index.html'


class AboutView(TemplateView):
    template_name = 'internet_banking/about.html'


class MyProfileView(DetailView):
    model = User

    template_name = 'internet_banking/my_profile.html'
    slug_field = 'url'
    # Имя переданного ключевого аргумента(именованной группы) в
    # URLConf, содержащего значение слага(slug). По умолчанию,
    # slug_url_kwarg это 'slug'.
    slug_url_kwarg = 'url'

    def get_data(self):
        accounts = User.objects.all()
        return accounts


def logout_user(request):
    logout(request)
    return redirect('home')
