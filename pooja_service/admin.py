from django.contrib import admin
from .models import PoojaService
from django.utils.html import strip_tags

@admin.register(PoojaService)
class AdminPoojaService(admin.ModelAdmin):
    list_display = ['title', 'short_describe', 'price', 'is_active']

    # HTML tags हटाकर सिर्फ शॉर्ट टेक्स्ट दिखाने के लिए
    def short_describe(self, obj):
        return strip_tags(obj.describe)[:50] + "..." if obj.describe else ""
    short_describe.short_description = "Details"