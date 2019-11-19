# Generated by Django 2.2 on 2019-10-20 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_fname', models.CharField(max_length=20)),
                ('customer_lname', models.CharField(max_length=20)),
                ('customer_password', models.CharField(max_length=20)),
                ('customer_dob', models.DateField(max_length=10)),
                ('customer_phone', models.CharField(max_length=10)),
                ('customer_address', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_img', models.FileField(upload_to='Image/')),
            ],
        ),
        migrations.CreateModel(
            name='Servicemen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_lname', models.CharField(max_length=20)),
                ('customer_fname', models.CharField(max_length=20)),
                ('customer_password', models.CharField(max_length=20)),
                ('customer_dob', models.DateField(max_length=10)),
                ('customer_qualicication', models.CharField(max_length=20)),
                ('customer_experience', models.CharField(max_length=20)),
                ('customer_address', models.CharField(max_length=1000)),
                ('customer_phone', models.CharField(max_length=10)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_password', models.CharField(max_length=20)),
                ('user_role', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=20)),
                ('user_otp', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Subservice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subservice_name', models.CharField(max_length=20)),
                ('subservice_details', models.CharField(max_length=100)),
                ('serviceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.ServiceType')),
                ('servicemenid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.Servicemen')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.User'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateField(max_length=10)),
                ('booking_status', models.CharField(max_length=10)),
                ('servicemenid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.Servicemen')),
                ('subserviceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.Subservice')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Eapp.Customer')),
            ],
        ),
    ]
