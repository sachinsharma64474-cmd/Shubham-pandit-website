# admin.py
from django.contrib import admin
from .models import PoojaBooking

@admin.register(PoojaBooking)
class PoojaBookingAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "mobile",
        "pooja",
        "pooja_date",
        "pooja_time",
        "status",
        "created_at",
    )
    list_filter = ("status", "pooja_date")
    search_fields = ("full_name", "mobile", "email")