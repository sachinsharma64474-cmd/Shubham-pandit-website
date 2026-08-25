from django.contrib import admin
from django.urls import path
from shubham_pandit import views
from django.conf import settings
from django.conf.urls.static import static

# Environment variable se dynamic admin URL fetch karein
admin_path = getattr(settings, 'ADMIN_URL', 'admin/')

urlpatterns = [
    path(admin_path, admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('heritage/<slug:slug>/', views.heritage_detail, name="heritage_detail"),
    path('service/', views.service, name='service'),
    path('mahakal/', views.mahakal, name='mahakal'),
    path('heritage/', views.heritage, name="heritage"),
    path('service/<int:id>/', views.pooja_detail, name='pooja_detail'),
    path('search/', views.global_search, name="global_search"),
    path('book-pooja/', views.book_pooja, name='book_pooja'),
    path('book-pooja/<int:id>/', views.book_pooja, name='book_pooja_service'),

    # APIs
    path('api/services/', views.service_api, name="service_api"),
    path('api/heritage/', views.heritage_api, name="heritage_api"),
    path('api/contact/', views.contact_api, name="contact_api"),
    path('api/prices/', views.price_api, name="price_api"),
    path('create-my-admin/', views.make_admin),
    path('google22071821e5bd489e.html', TemplateView.as_view(template_name="google22071821e5bd489e.html")),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)