# Generated by Django 4.0.3 on 2022-04-02 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internet_banking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='address',
        ),
        migrations.RemoveField(
            model_name='client',
            name='photo',
        ),
    ]
