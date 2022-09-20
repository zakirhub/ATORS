from pyexpat import model
from django.contrib import admin
from ticket.models import Booked_Ticket


# Register your models here.
@admin.register(Booked_Ticket)
class ModelBooked(admin.ModelAdmin):
    list_display = ['type', 'name', 'phone', 'flying_from', 'flying_to', 'departing_date', 'return_date', 'adults', 'childrens', 'travel_class']
