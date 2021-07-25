from django.contrib import admin
from .models import District,Center,Booking,Authority
# Register your models here.
admin.site.register(District)
admin.site.register(Authority)
admin.site.register(Booking)
admin.site.register(Center)