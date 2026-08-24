"""
ASGI config for shubham_pandit project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shubham_pandit.settings')

application = get_asgi_application()