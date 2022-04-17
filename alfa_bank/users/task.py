from django.core.mail import send_mail

from alfa_bank.celery import app
from alfa_bank.settings import DEFAULT_FROM_EMAIL


@app.task()
def post_email(username, foremail):
    send_mail(f'Пользователь с именем {username} был'
              f' зарегистрирован на вашу почту', 'Если это были не вы, просто проигнорируйте это письмо',
              DEFAULT_FROM_EMAIL, foremail)

@app.task()
def post_email_loan(credit, time, foremail):
    send_mail(f'На ваш аккаунт был оформлен кредит, на сумму {credit} бел. руб.!',
              f'Кредит был оформлен на {time} месяцев на сумму {credit} бел. руб. '
              f'Если оформили его не вы, срочно позвоните нам. Сайт alfa-bank.by',
              DEFAULT_FROM_EMAIL, foremail)

# redis-server
#  celery -A alfa_bank worker -l info -P eventlet
