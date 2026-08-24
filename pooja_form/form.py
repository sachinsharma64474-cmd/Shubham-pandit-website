# form.py
from django import forms
from .models import PoojaBooking

class PoojaBookingForm(forms.ModelForm):

    class Meta:
        model = PoojaBooking
        # 🌟 "status" ko yahan add karein
        exclude = ("pooja", "status", "created_at","updated_at")

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "mobile": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "address": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "pincode": forms.TextInput(attrs={"class": "form-control"}),
            "pooja_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "pooja_time": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
        }