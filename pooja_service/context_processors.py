from .models import PoojaService

def footer_poojas(request):
    # Sirf pehli 5 active pooja services fetch karega
    return {
        'footer_poojas': PoojaService.objects.filter(is_active=True).order_by('?')[:5]
    }