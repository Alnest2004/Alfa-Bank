from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_support = models.BooleanField(default=False, verbose_name="It's support")
    address = models.TextField(blank=True, max_length=100, verbose_name="client address")
    photo = models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Photo")
    email = models.EmailField(max_length=100, unique=True)
    url = models.SlugField(max_length=130, unique=False)

    def save(self, *args, **kwargs):
        self.url = self.username
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    def get_sum_loans(self):
        from internet_banking.models import Account
        from internet_banking.models import Loans
        accounts = Account.objects.filter(user=self.pk).first().id
        try:
            sum = 0
            paid = 0
            for acc in Loans.objects.filter(account_id=accounts).all():
                sum = sum + acc.Credit_amount
                paid = paid + acc.Paid_out
            return sum - paid
        except:
            return 0

    def get_number_loans(self):
        from internet_banking.models import Account
        from internet_banking.models import Loans
        accounts = Account.objects.filter(user=self.pk).first().id
        try:
            kol = Loans.objects.filter(account_id=accounts).count()
            return kol
        except:
            return 0
