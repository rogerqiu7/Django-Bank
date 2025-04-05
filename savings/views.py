from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Savings
from .serializers import SavingsSerializer
from django.shortcuts import get_object_or_404
from bson import ObjectId

# API view for handling collections of savings accounts
# Supports listing all accounts and creating new ones
class SavingsList(APIView):
    # GET /api/savings/
    # Returns a list of all savings accounts
    def get(self, request):
        accounts = Savings.objects.all()                  # Retrieve all accounts from the database
        serializer = SavingsSerializer(accounts, many=True)  # Convert queryset to JSON-serializable data
        return Response(serializer.data)                  # Return serialized data with 200 OK status

    # POST /api/savings/
    # Creates a new savings account with the data sent in the request body
    def post(self, request):
        serializer = SavingsSerializer(data=request.data)    # Create serializer with request data
        if serializer.is_valid():                           # Validate the data
            serializer.save()                               # Save the new account to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return 201 Created with new account
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return 400 Bad Request if invalid

# API view for handling individual savings accounts for retrieving, updating, and deleting accounts by ID
class SavingsDetail(APIView):

    # Helper method to fetch a savings account by its MongoDB ObjectId
    def get_object(self, id):
        return get_object_or_404(Savings, _id=ObjectId(id))  # Casts string to ObjectId for Mongo lookup

    # GET /api/savings/<id>/
    # Returns a savings account by its ID if found; otherwise raises a 404 Not Found error
    def get(self, request, id):
        account = self.get_object(id)          
        if account:
            serializer = SavingsSerializer(account)  # Serialize the account
            return Response(serializer.data)        # Return serialized data with 200 OK
        return Response(status=status.HTTP_404_NOT_FOUND)  # Fallback 404 (not usually reached due to get_object_or_404)

    # PUT /api/savings/<id>/
    # Updates an existing account by ID using data from the request body
    def put(self, request, id):
        account = self.get_object(id)                   # Get the account or 404
        if not account:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found
        serializer = SavingsSerializer(account, data=request.data)  # Create serializer with existing account and new data
        if serializer.is_valid():                       # Validate the data
            serializer.save()                           # Save the updated account
            return Response(serializer.data)            # Return updated account with 200 OK
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return 400 if invalid

    # DELETE /api/savings/<id>/
    # Deletes the account by ID
    def delete(self, request, id):
        account = self.get_object(id)                   # Get the account or 404
        if not account:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found
        account.delete()                               # Delete the account from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content