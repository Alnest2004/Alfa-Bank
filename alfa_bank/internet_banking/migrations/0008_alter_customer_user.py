# Generated by Django 4.0.3 on 2022-04-12 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('internet_banking', '0007_alter_customer_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client_user', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
