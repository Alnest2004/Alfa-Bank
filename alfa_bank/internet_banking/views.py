from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from rest_framework.decorators import permission_classes, api_view

from alfa_bank.celery import app
from alfa_bank.settings import RECIPIENTS_EMAIL
from internet_banking.forms import CreateTransferForm, CreateLoanForm, ReviewForm
from internet_banking.models import Account, Reviews
from internet_banking.services import make_transfer, filter_user_account, check_account_exists, make_loan, comis_loan, \
    make_review
from users.models import User
from decimal import Decimal

from users.task import post_email_loan
from rest_framework.permissions import IsAuthenticated


class HomePageView(ListView):
    model = Reviews
    template_name = 'internet_banking/index.html'
    context_object_name = "reviews_object"

    def get_queryset(self):
        return Reviews.objects.order_by('-pk')[0:3]



class AboutView(TemplateView):
    template_name = 'internet_banking/about.html'


class MyProfileView(LoginRequiredMixin, DetailView):
    model = User
    permission_classes = [IsAuthenticated]

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
            return render(request, "internet_banking/success.html", )
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/create_transfer.html", {'form': form})


@app.task()
def LoanProcessingView(request):
    if request.method == 'GET':
        form = CreateLoanForm()
    elif request.method == 'POST':
        submit_button = request.POST.get('submit_button')
        if submit_button == 'credit':
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

                message = f"Кредит на сумму {request.POST['Credit_amount']} бел.руб. успешно оформлен," \
                          f" спасибо что выбрали нас! С уважением Альфа-Банк"
                return render(request, "internet_banking/loan_processing.html", {'form': form, 'mess': message})
        else:
            form = CreateLoanForm(data=request.POST)
            if form.is_valid() and request.recaptcha_is_valid:
                monthly_payment = (Decimal(request.POST['Credit_amount']) / Decimal(
                    request.POST['time'])) / 100 * comis_loan + (Decimal(request.POST['Credit_amount']) / Decimal(
                    request.POST['time']))
                monthly_payment = float("%.2f" % monthly_payment)
                return render(request, "internet_banking/loan_processing.html",
                              {'form': form, 'monthly_payment': monthly_payment})

    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/loan_processing.html", {'form': form})


def handler404(request, *args, **kwargs):
    return render(request, "errors/404.html", status=404)


def handler403(request, *args, **kwargs):
    return render(request, "errors/403.html", status=403)


def handler500(request, *args, **kwargs):
    return render(request, "errors/500.html", status=500)


def CreateReviewView(request):
    if request.method == 'GET':
        form = ReviewForm()
    elif request.method == 'POST':
        form = ReviewForm(data=request.POST)

        if form.is_valid():
            messages.success(request, "Message sent successfully!")

            make_review(
                request.user,
                request.POST['text']
            )
        return render(request, "internet_banking/reviews.html", {'form': form})
    else:
        return HttpResponse('Неверный запрос. ')
    return render(request, "internet_banking/reviews.html", {'form': form})
