from django.contrib import admin
from .models import PoojaService

@admin.register(PoojaService)
class AdminPoojaService(admin.ModelAdmin):
    list_display = ['title', 'describe', 'img','price']

