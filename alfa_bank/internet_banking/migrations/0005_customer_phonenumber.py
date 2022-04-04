# Generated by Django 4.0.3 on 2022-04-04 18:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_banking', '0004_loans_remove_transaction_account_transfer_commission_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phoneNumber',
            field=models.CharField(max_length=16, null=True, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
