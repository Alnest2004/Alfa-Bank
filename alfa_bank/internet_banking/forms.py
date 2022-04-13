from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError

from internet_banking.models import Account, Customer, Transfer
from internet_banking.services import com
from users.models import User


class CreateTransferForm(forms.ModelForm):
    # widget.attrs['readonly'] = True
    commission = forms.DecimalField(label='Комиссия',
                                    widget=forms.TextInput(attrs={'readonly': 'readonly'}),
                                    initial=com)

    def clean_to_account(self):
        form_account = self.cleaned_data.get('to_account')
        existing = User.objects.filter(username=form_account)
        if not existing:
            raise ValidationError('Такого пользователя нету')

        return form_account


    class Meta:
        model = Transfer
        exclude = ['from_account']

