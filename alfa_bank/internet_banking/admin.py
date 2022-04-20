from django.contrib import admin
from internet_banking.models import (Customer, Account,
                                     Action, Transfer, Loans,
                                     Reviews)

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Action)
admin.site.register(Transfer)
admin.site.register(Loans)
admin.site.register(Reviews)
