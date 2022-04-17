import traceback

from django.contrib.auth import logout
from django.core.mail import BadHeaderError
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from rest_framework import viewsets, mixins

from alfa_bank.celery import app
from alfa_bank.settings import RECIPIENTS_EMAIL
from internet_banking.forms import CreateTransferForm, CreateLoanForm
from internet_banking.models import Account, Transfer
from internet_banking.services import make_transfer, filter_user_account, check_account_exists, make_loan
from users.models import User
from decimal import Decimal

from users.task import post_email_loan


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
        form = CreateTransferForm(data=request.POST)
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
            return render(request, "internet_banking/success.html",)
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/create_transfer.html", {'form': form})

@app.task()
def LoanProcessingView(request):
    if request.method == 'GET':
        form = CreateLoanForm()
    elif request.method == 'POST':
        form = CreateLoanForm(data=request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            twoattr = Account.objects.filter(user=request.user)[:1]

            from_account = filter_user_account(
                request.user,
                twoattr
            )

            make_loan(
                from_account,
                request.POST['Credit_amount'],
                request.POST['time']
            )

            # email = form.cleaned_data['email']
            email = request.user.email
            RECIPIENTS_EMAIL.append(email)
            try:
                post_email_loan.delay(
                    request.POST['Credit_amount'],
                    request.POST['time'],
                    RECIPIENTS_EMAIL
                )
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')

            return render(request, "internet_banking/loan_processing.html", {'form': form})
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/loan_processing.html", {'form': form})



def handler404(request, *args, **kwargs):
    return render(request, "errors/404.html", status=404)


def handler403(request, *args, **kwargs):
    return render(request, "errors/403.html", status=403)


def handler500(request, *args, **kwargs):
    return render(request, "errors/500.html", status=500)
