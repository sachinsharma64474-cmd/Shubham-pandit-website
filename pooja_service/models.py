from django.db import models
from tinymce.models import HTMLField

class PoojaService(models.Model):
    # Basic Info
    title = models.CharField(max_length=100, verbose_name="Pooja Ka Naam")
    describe = HTMLField(verbose_name="Pooja Ke Baare Mein Details")
    img = models.ImageField(upload_to='pooja/', blank=True, null=True, verbose_name="Pooja Ki Photo")
    
    # Price Fields
    price = models.IntegerField(default=0, verbose_name="Actual Price (₹)")
    # default=0 hata kar default=None ya blank=True rakhna behtar hai, taaki agar discount na ho toh 0 na dikhe
    discount_price = models.IntegerField(blank=True, null=True, verbose_name="Offer Price (₹) [Optional]")  

    # 🌟 Fixed: 'placeholder' ki jagah 'help_text' use kiya hai
    duration = models.CharField(
        max_length=50, 
        blank=True, 
        null=True, 
        verbose_name="Pooja Ka Samay",
        help_text="e.g., 2-3 Ghante"
    )
    
    samagri_included = models.BooleanField(default=True, verbose_name="Kya Samagri Price Mein Shamil Hai?")
    is_online_available = models.BooleanField(default=False, verbose_name="Kya Video Call Par Pooja Ho Sakti Hai?")
    
    # 🌟 Fixed: Yahan bhi 'placeholder' ki jagah 'help_text' kiya hai
    badge = models.CharField(
        max_length=30, 
        blank=True, 
        null=True, 
        verbose_name="Special Tag/Badge",
        help_text="e.g., Best Seller, Trending"
    )

    is_active = models.BooleanField(default=True, verbose_name="Website Par Dikhayein?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Pooja Services"