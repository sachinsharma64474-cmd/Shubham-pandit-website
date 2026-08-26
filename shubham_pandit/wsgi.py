import os
import pymysql

# Aiven MySQL ke liye driver bind karein (Settings load hone se PEHLE)
pymysql.install_as_MySQLdb()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shubham_pandit.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Vercel Serverless Function handler
app = application