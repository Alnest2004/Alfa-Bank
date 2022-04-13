from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from rest_framework import viewsets, mixins

from internet_banking.forms import CreateTransferForm
from internet_banking.models import Account, Transfer
from internet_banking.services import make_transfer, filter_user_account, check_account_exists
from users.models import User
from decimal import Decimal

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
#
#
# class ActionViewSet(viewsets.GenericViewSet,
#                     mixins.ListModelMixin,
#                     mixins.CreateModelMixin):

def CreateTransfer(request):
    if request.method == 'GET':
        form = CreateTransferForm()
    elif request.method == 'POST':
        form = CreateTransferForm(request.POST)
        if form.is_valid():
            twoattr = Account.objects.filter(user=request.user)[:1]

            from_account = filter_user_account(
                request.user,
                twoattr
            )

            to_account = check_account_exists(request.POST['to_account'])

            make_transfer(
                from_account,
                to_account,
                Decimal(request.POST['amount'])
            )
            return redirect('home')
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/addcustomer.html", {'form': form})


