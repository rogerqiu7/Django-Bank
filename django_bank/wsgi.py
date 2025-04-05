import os
from django.core.wsgi import get_wsgi_application

# Set the settings module for the WSGI application
# This is required for the app to run in production environments
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_bank.settings")

# Initialize the WSGI application for deployment
application = get_wsgi_application()