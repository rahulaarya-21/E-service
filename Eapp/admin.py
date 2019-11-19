from django.contrib import admin
from .models import *
# Register your models here.

class userdetails(admin.ModelAdmin):
    list_display=('user_role','user_email')

admin.site.register(User,userdetails)
admin.site.register(Customer)
admin.site.register(Servicemen)
admin.site.register(ServiceType)
admin.site.register(Subservice)
admin.site.register(Booking)
admin.site.register(Image)

