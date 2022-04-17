from decimal import Decimal

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models


class Customer(models.Model):
    fname = models.CharField(max_length=100, unique=False)
    lname = models.CharField(max_length=100, unique=False)
    pname = models.CharField(max_length=100, unique=False)
    city = models.CharField(max_length=255, unique=False)
    house = models.TextField(max_length=255, unique=False)
    photo = models.ImageField(upload_to="clients/%Y/%m/%d", null=True, blank=True)

    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="client_user",
                             on_delete=models.CASCADE, verbose_name="User", default=None, blank=True)

    # service = models.ForeignKey('TypeService', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.pname}'


class Account(models.Model):
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="account_user",
                             on_delete=models.PROTECT, verbose_name="User")

    def __str__(self):
        return f'{self.user.username}'




class Action(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='actions',
    )

    def __str__(self):
        return f'Account number {self.account.id} ' + \
               f'was changed on {str(self.amount)}'


class Transfer(models.Model):
    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account',
        blank=True,
        null=True
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )

    amount = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )

    commission = models.DecimalField(
        default=1.2,
        max_digits=12,
        decimal_places=2
    )

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)




class Loans(models.Model):
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account_loans'
    )
    Credit_amount = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    Paid_out = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )
    time = models.IntegerField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Credit_amount)
