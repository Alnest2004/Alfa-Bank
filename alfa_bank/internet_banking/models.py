from django.conf import settings
from django.db import models
from django.urls import reverse
from users.models import User


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    pname = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="clients/%Y/%m/%d", null=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="client_user",
                             on_delete=models.CASCADE, verbose_name="User")

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
        return f'{self.id} of {self.user.username}'


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


class Transaction(models.Model):
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE
    )

    merchant = models.CharField(max_length=255)

    def __str__(self):
        return f'Account number {self.account.id} ' + \
               f'sent {str(self.amount)} to {self.merchant}'


class Transfer(models.Model):
    from_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='from_account'
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='to_account'
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )


class Interest(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
    )

    amount = models.DecimalField(
        decimal_places=2,
        max_digits=12,
    )
