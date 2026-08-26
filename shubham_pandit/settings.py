from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Secret Key strictly loaded from environment
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY: Debug status parsed safely
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = ['*']
# Application definition
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    
    # 🌟 Cloudinary को staticfiles से पहले होना ज़रूरी है
    'cloudinary_storage',
    "django.contrib.staticfiles",
    'cloudinary',

    'tinymce',
    'pooja_service',
    'heritage_places',
    "pooja_form",
    "Gallery",
    'django.contrib.sitemaps',
]




JAZZMIN_SETTINGS = {
    "site_title": "My Admin",
    "site_header": "My Website",
    "site_brand": "Admin Panel",
    "welcome_sign": "Welcome to Dashboard",
    "copyright": "© 2026 My Company",
    "site_url": "/", 
    "topmenu_links": [
        {"name": "View Site", "url": "/", "new_window": True},
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shubham_pandit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'template'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shubham_pandit.context_processors.footer_services',
                'pooja_service.context_processors.footer_poojas',
            ],
        },
    },
]

WSGI_APPLICATION = 'shubham_pandit.wsgi.application'

# Database Setup
# Database Setup
# Database Setup
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.getenv('DB_NAME', 'defaultdb'),
        'USER': os.getenv('DB_USER', 'avnadmin'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'AVNS_tDbEzgX4ZlPzfBf4TAE'),
        'HOST': os.getenv('DB_HOST', 'shubhampanditdb-shubhampanditwebsite.k.aivencloud.com'),
        'PORT': os.getenv('DB_PORT', '20485'),
        'OPTIONS': {
            'ssl': {
                'check_hostname': False,
            }
        }
    }
}
# Cache configuration
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# Static & Media files
# Static & Media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Security Settings for Production
if not DEBUG:
    SECURE_SSL_REDIRECT = False  # Vercel internal SSL के लिए इसे False रखें
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

# WhiteNoise Configuration for Static Files
# Static files (CSS, JavaScript, Images)
# Static files (CSS, JavaScript, Images)
# Static Files Setup for Vercel WhiteNoise
# Static files (CSS, JavaScript, Images)
# settings.py

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🌟 Cloudinary Storage Setup (For Uploaded Media Files)
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME', 'ga3nlcvh'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY', '641478899823584'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET', 'uNkkKvDzXu3L_xMMM6jgaqWNagw'),
}

# 🌟 Backward Compatibility Keys for 'cloudinary_storage' package
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

# 🌟 Django 4.2+ STORAGES Dict
STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

WHITENOISE_MANIFEST_STRICT = False

# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    "license_key": "gpl",
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "plugins": "advlist autolink lists link image charmap preview anchor "
               "searchreplace visualblocks code fullscreen insertdatetime media table help wordcount",
    "toolbar": "undo redo | formatselect | "
               "bold italic backcolor | alignleft aligncenter "
               "alignright alignjustify | bullist numlist outdent indent | "
               "removeformat | help",
}