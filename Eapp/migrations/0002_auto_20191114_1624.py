# Generated by Django 2.2 on 2019-11-14 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Eapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_fname',
            new_name='customer_name',
        ),
        migrations.RenameField(
            model_name='servicemen',
            old_name='customer_experience',
            new_name='customer_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_dob',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_lname',
        ),
        migrations.RemoveField(
            model_name='servicemen',
            name='customer_dob',
        ),
        migrations.RemoveField(
            model_name='servicemen',
            name='customer_fname',
        ),
        migrations.RemoveField(
            model_name='servicemen',
            name='customer_lname',
        ),
        migrations.RemoveField(
            model_name='servicemen',
            name='customer_qualicication',
        ),
        migrations.AlterField(
            model_name='servicemen',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.User'),
        ),
    ]
