from django.db import models
from pooja_service.models import PoojaService

class PoojaBooking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    pooja = models.ForeignKey(
        PoojaService,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    pooja_date = models.DateField()
    pooja_time = models.TimeField()

    # 🌟 Status Field default value ke sath add karein
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def __str__(self):
        return f"{self.full_name} - {self.pooja.title}"