from django.contrib import admin
from .models import HeritagePlace

@admin.register(HeritagePlace)
class HeritagePlaceAdmin(admin.ModelAdmin):
    # Admin list view me kaun-kaun se columns dikhenge
    list_display = ('title', 'slug', 'description_short')
    
    # Title ke basis par slug automatic generate ho jayega (Aapko manually type nahi karna padega)
    prepopulated_fields = {'slug': ('title',)}
    
    # Search bar add karne ke liye
    search_fields = ('title', 'description')

    # Description agar badi ho toh list me short dikhane ke liye custom method
    def description_short(self, obj):
        if len(obj.description) > 50:
            return f"{obj.description[:50]}..."
        return obj.description
    description_short.short_description = "Description"