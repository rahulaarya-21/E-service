# Generated by Django 2.2 on 2019-11-14 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0002_auto_20191114_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicemen',
            old_name='customer_address',
            new_name='servicemen_address',
        ),
        migrations.RenameField(
            model_name='servicemen',
            old_name='customer_name',
            new_name='servicemen_name',
        ),
        migrations.RenameField(
            model_name='servicemen',
            old_name='customer_phone',
            new_name='servicemen_phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_password',
        ),
        migrations.RemoveField(
            model_name='servicemen',
            name='customer_password',
        ),
    ]
