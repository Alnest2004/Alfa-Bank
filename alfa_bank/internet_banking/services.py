from decimal import Decimal

from django.db import transaction
from django.core.exceptions import ValidationError

from internet_banking.models import Transfer, Account, Loans, Reviews

com = Decimal("1.2")
comis_loan = Decimal("2.9")

def make_transfer(from_account, to_account, amount):
    if from_account.balance < amount:
        raise (ValueError('Не достаточно средств'))
    if from_account == to_account:
        raise (ValueError('Выберите другой аккаунт'))

    with transaction.atomic():
        from_balance = from_account.balance - amount -\
                       (amount*(com)/100)
        from_account.balance = from_balance
        from_account.save()

        to_balance = to_account.balance + amount
        to_account.balance = to_balance
        to_account.save()

        transfer = Transfer.objects.create(
            from_account=from_account,
            to_account=to_account,
            amount=amount,
            commission=com
        )

    return transfer

def make_loan(from_account, credit_amount, time):


    loan = Loans.objects.create(
        account = from_account,
        Credit_amount = credit_amount,
        time = time,
    )

    return loan

def make_review(from_user, text):

    review = Reviews.objects.create(
        user = from_user,
        text = text
    )

    return review



def filter_user_account(user, account_id):
    try:
        account = Account.objects.filter(
            user=user).get(pk=account_id)
    except (Account.DoesNotExist):
        raise ValidationError("Account doesn't exist")

    return account


def check_account_exists(account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Exception as e:
        print(e)
        raise ValueError('No such account')

    return account
