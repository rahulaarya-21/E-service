from django.db import models

# Create your models here.

class User(models.Model):
    user_password=models.CharField(max_length=20)
    user_role=models.CharField(max_length=20)
    user_email=models.EmailField(max_length=20)
    user_otp=models.CharField(max_length=6)


class Customer(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    customer_name=models.CharField(max_length=20)
    #customer_password=models.CharField(max_length=20)
    customer_phone=models.CharField(max_length=10)
    customer_address=models.CharField(max_length=1000)


class Servicemen(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    servicemen_name=models.CharField(max_length=20)
    #servicemen_password=models.CharField(max_length=20)
    servicemen_phone=models.CharField(max_length=10)
    servicemen_address=models.CharField(max_length=1000)

class ServiceType(models.Model):
    service_name=models.CharField(max_length=20)

class Subservice(models.Model):
    servicemenid=models.ForeignKey(Servicemen,on_delete=models.CASCADE)
    serviceid=models.ForeignKey(ServiceType,on_delete=models.CASCADE)
    subservice_name=models.CharField(max_length=20)
    subservice_details=models.CharField(max_length=100)

class Booking(models.Model):
    servicemenid=models.ForeignKey(Servicemen,on_delete=models.CASCADE)
    userid=models.ForeignKey(Customer,on_delete=models.CASCADE)
    subserviceid=models.ForeignKey(Subservice,on_delete=models.CASCADE)
    booking_date=models.DateField(max_length=10)
    booking_status=models.CharField(max_length=10)

class Image(models.Model):
    upload_img=models.FileField(upload_to='Image/')


