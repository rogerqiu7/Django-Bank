from pathlib import Path

# BASE_DIR is the root directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key used for cryptographic signing. Should be changed in production.
SECRET_KEY = 'your-secret-key'
# Debug mode enables detailed error pages and should be set to False in production.
DEBUG = True
# List of host/domain names that this Django site can serve.
ALLOWED_HOSTS = []

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# List of Django applications that are enabled in this project.
# These include Django's built-in apps and custom project apps.
INSTALLED_APPS = [
    'django.contrib.auth',          # Authentication framework
    'django.contrib.contenttypes',  # Framework for content types
    'django.contrib.sessions',      # Session framework
    'django.contrib.messages',      # Messaging framework
    'django.contrib.staticfiles',   # Framework for managing static files
    'rest_framework',               # Django REST framework for building APIs
    'savings',                      # my app for handling savings accounts
]

# List of middleware components that process requests/responses globally.
# They're executed in order (top to bottom for requests, bottom to top for responses).
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',           # Security enhancements
    'django.contrib.sessions.middleware.SessionMiddleware',    # Manages sessions across requests
    'django.middleware.common.CommonMiddleware',               # Common functionality
    'django.middleware.csrf.CsrfViewMiddleware',               # Cross-Site Request Forgery protection
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Associates users with requests
    'django.contrib.messages.middleware.MessageMiddleware',    # Enables messaging system
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

# Root URL configuration module
ROOT_URLCONF = 'django_bank.urls'

# Configuration for template engines, required for Postman GUI
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can add template folders here if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application path for production deployment
WSGI_APPLICATION = 'django_bank.wsgi.application'

# MongoDB database configuration for the project
# Using djongo as the database engine (Django + MongoDB connector)
DATABASES = {
    'default': {
        'ENGINE': 'djongo',                  # MongoDB connector for Django
        'NAME': 'django_bank',               # Database name
        'CLIENT': {                          # MongoDB connection parameters
            'host': 'mongodb+srv://Cluster57205:ZnZifVhTe2FO@cluster57205.wswiz.mongodb.net/django_bank', # Connection string of my cluster in MongoDB Atlas
        }
    }
}

# URL prefix for static files (CSS, JavaScript, Images), required for Postman GUI
STATIC_URL = '/static/'