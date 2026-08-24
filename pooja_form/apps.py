# pooja_form/apps.py
from django.apps import AppConfig

class PoojaFormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pooja_form'
    
    # 🌟 Admin panel par app ka naam badalne ke liye ye line add karein
    verbose_name = "Booking"
