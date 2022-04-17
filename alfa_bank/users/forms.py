from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError

from internet_banking.models import Account, Customer
from users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists():
    #         raise ValidationError('Пользователь с таким именем уже есть')
    #     return username


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class RegisterCustomerForm(forms.ModelForm):
    fname = forms.CharField(label='Имя')
    lname = forms.CharField(label='Фамилия')
    pname = forms.CharField(label='Отчество')
    city = forms.CharField(label='Город')
    house = forms.CharField(label='Дом')
    photo = forms.ImageField(label='Ваше фото',required=False)
    phoneNumber = forms.CharField(label='Номер телефона')
    # user = forms.IntegerField(label='Пользователь', widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Customer
        exclude = ['user', ]

    # def validate(self):
