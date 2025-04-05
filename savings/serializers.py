from rest_framework import serializers
from .models import Savings

# Serializer for the Savings model that converts between Python objects and JSON
# Handles validation, serialization, and deserialization of Savings data
class SavingsSerializer(serializers.ModelSerializer):
    # Make the ID field read-only since it's auto-generated
    _id = serializers.CharField(read_only=True)
    
    # Configure the serializer to work with the Savings model
    class Meta:
        model = Savings           # The model to serialize/deserialize
        fields = '__all__'        # Include all fields from the model