import factory
from faker import Faker

from internet_banking.models import Account, Transfer, Loans

fake = Faker()

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'

class User2Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = 'True'
    email = "test@gmail.com"


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    balance = '5.99'
    user = factory.SubFactory(UserFactory)

class Account2Factory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account

    balance = '6.99'
    user = factory.SubFactory(User2Factory)


class TransferFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transfer

    from_account = factory.SubFactory(AccountFactory)
    to_account = factory.SubFactory(Account2Factory)
    amount = '3.23'
    commission = '3.88'

class LoanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Loans

    account = factory.SubFactory(AccountFactory)
    Credit_amount = "99.32"
    Paid_out = "11"
    time = "5"
