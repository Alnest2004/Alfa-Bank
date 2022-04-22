from decimal import Decimal

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError

from internet_banking.models import Account, Customer, Transfer, Loans, Reviews
from internet_banking.services import com
from users.models import User


class CreateTransferForm(forms.ModelForm):
    #
    # def __init__(self, user, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['from_account'] = str(User.objects.filter(pk=user.id)[:1])
    #     print("Поле FROM_ACCOUNT = " + str(self.fields['from_account']))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['to_account'].empty_label = "Выберите пользователя"

    # from_account = forms.CharField(label='От кого')

    commission = forms.DecimalField(label='Комиссия в %',
                                    widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                                    initial=com)
    amount = forms.DecimalField(label='Сумма')

    to_account = forms.ModelChoiceField(label='Кому', queryset=Account.objects.all())

    # to_account = forms.CharField(label='Кому')

    def clean_to_account(self):
        form_account = self.cleaned_data.get('to_account')
        existing = User.objects.filter(username=form_account)
        if not existing:
            raise ValidationError('Такого пользователя нету')

        return form_account

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise ValidationError('Введите положительное число')

        return amount

    class Meta:
        model = Transfer
        exclude = ['from_account', ]


class CreateLoanForm(forms.ModelForm):
    Credit_amount = forms.DecimalField(label='Желаемая сумма', max_value=10000, min_value=100)
    time = forms.IntegerField(label='На какой срок', max_value=32, min_value=1)
    income = forms.DecimalField(label='Ваш доход в месяц')

    def clean_income(self):
        amount = self.cleaned_data.get('Credit_amount')
        income = self.cleaned_data.get('income')
        if income < (amount / 5):
            raise ValidationError('Доход должен быть не меньше 20% от суммы кредита')

        return income

    class Meta:
        model = Loans
        exclude = ['account', 'Paid_out']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("text",)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border", "maxlength": "10"})
        }
