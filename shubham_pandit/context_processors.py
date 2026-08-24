from pooja_service.models import PoojaService

def footer_services(request):
    return {
        'footer_services': PoojaService.objects.filter(is_active=True)[:4]
    }
