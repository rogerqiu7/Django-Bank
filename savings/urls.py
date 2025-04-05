from django.urls import path
from .views import SavingsList, SavingsDetail

# URL patterns for the savings app
# Maps URL paths to view classes that handle the requests
urlpatterns = [
    path('api/savings/', SavingsList.as_view()),          # Endpoint for list operations (GET all, POST new)
    path('api/savings/<str:id>/', SavingsDetail.as_view()), # Endpoint for detail operations (GET one, PUT, DELETE)
]