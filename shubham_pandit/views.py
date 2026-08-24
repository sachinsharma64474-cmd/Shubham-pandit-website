from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
from pooja_service.models import PoojaService
from heritage_places.models import HeritagePlace
from pooja_form.form import PoojaBookingForm
from django.http import JsonResponse


def global_search(request):
    query = request.GET.get("search", "").strip()

    services = PoojaService.objects.none()
    places = HeritagePlace.objects.none()

    if query:
        services = PoojaService.objects.filter(
            Q(title__icontains=query) |
            Q(describe__icontains=query),
            is_active=True
        )

        places = HeritagePlace.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    context = {
        "query": query,
        "services": services,
        "places": places,
    }

    return render(request, "search.html", context)


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def heritage(request):
    query = request.GET.get("search", "").strip()

    if query:
        places = HeritagePlace.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        places = HeritagePlace.objects.all()

    return render(request, "heritage.html", {
        "heritage_places": places
    })

def heritage_detail(request, slug):
    place = get_object_or_404(HeritagePlace, slug=slug)
    return render(request, "heritage_detail.html", {
        "place": place
    })
def service(request):
    # Pooja services ke liye active check aur dynamic url search fallback
    query = request.GET.get('search', '').strip()
    if query:
        services = PoojaService.objects.filter(
            Q(title__icontains=query) | Q(describe__icontains=query),
            is_active=True
        )
    else:
        services = PoojaService.objects.filter(is_active=True)
        
    return render(request, 'service.html', {'k': services})

# 🌟 NAYA VIEW: Single Pooja Detail Page ke liye
def pooja_detail(request, id):
    # Id ke basis par single pooja object nikalenge, nahi mila toh 404 error
    pooja = get_object_or_404(PoojaService, id=id)
    return render(request, 'pooja_detail.html', {'pooja': pooja})

def mahakal(request):
    k = PoojaService.objects.all()
    return render(request, 'mahakal.html', {'k': k})




def book_pooja(request, id=None):
    selected_pooja = None

    if id:
        selected_pooja = get_object_or_404(PoojaService, id=id)

    if request.method == "POST":
        form = PoojaBookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            if selected_pooja:
                booking.pooja = selected_pooja
            else:
                pooja_id = request.POST.get("pooja")
                if pooja_id:
                    booking.pooja = get_object_or_404(PoojaService, id=pooja_id)

            booking.save() # 🌟 Yahan database mein final entry hoti hai
            return redirect("service")
        else:
            # 🌟 Agar form me koi error aaye toh Terminal (VS Code) par print hoga
            print("Form Errors:", form.errors)

    else:
        form = PoojaBookingForm()

    return render(request, "book_pooja.html", {
        "form": form,
        "selected_pooja": selected_pooja,
        "poojas": PoojaService.objects.filter(is_active=True)
    })

def service_api(request):
    services = PoojaService.objects.filter(is_active=True)

    data = []

    for s in services:
        data.append({
            "id": s.id,
            "title": s.title,
            "price": s.price,
            "discount_price": s.discount_price,
            "duration": s.duration,
            "badge": s.badge,
            "online": s.is_online_available,
        })

    return JsonResponse(data, safe=False)



def heritage_api(request):
    places = HeritagePlace.objects.all()

    data = []

    for p in places:
        data.append({
            "title": p.title,
            "slug": p.slug,
            "description": p.description,
        })

    return JsonResponse(data, safe=False)



def contact_api(request):

    data = {
        "name": "Shubham Pandit Ji",
        "phone": "+91 9131648738",
        "email": "panditji@gmail.com",
        "address": "Ujjain, Madhya Pradesh"
    }

    return JsonResponse(data)



def price_api(request):

    services = PoojaService.objects.filter(is_active=True)

    data = []

    for s in services:
        data.append({
            "title": s.title,
            "price": s.price,
            "offer_price": s.discount_price,
        })

    return JsonResponse(data, safe=False)



def contact(request):
    return render(request,"contact.html")

def gallery(request):
    return render(request,"Gallery.html")    


from django.contrib.auth.models import User
from django.http import HttpResponse

def make_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@gmail.com", "Admin@1234")
        return HttpResponse("Superuser Created! Username: admin, Password: Admin@1234")
    return HttpResponse("Admin user already exists!")