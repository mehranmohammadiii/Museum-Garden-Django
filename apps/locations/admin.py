from django.contrib import admin
from .models import Locations,VisitorType,Ticket,Contact
# Register your models here.

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ("title","image_name","visiting_days","visiting_hours","register_date")

@admin.register(VisitorType)
class VisitortypeAdmin(admin.ModelAdmin):
    list_display = ("name" , )

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("visitortype","location","price")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name","subject","register_date","is_seen","email")