from django.urls import path, include

# URL patterns for the entire project
# Routes all requests to the savings app's URL configuration
urlpatterns = [
    path('', include('savings.urls')),  # Delegate handling to the savings app's URL patterns
]