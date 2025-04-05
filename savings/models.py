from djongo import models  # instead of django.db.models

'''
    This class represents the structure of a "savings account" record in the database.
    Django ORM uses this model to create and interact with the corresponding MongoDB collection.
    The Savings class maps directly to a MongoDB collection called savings
    Each instance of Savings maps to a MongoDB document
    Fields like first_name, savings_amount become document fields
    _id = models.ObjectIdField(...) maps directly to MongoDB's native _id field
'''

class Savings(models.Model):
    # Primary key field (auto-incrementing ID) for uniquely identifying each account
    _id = models.ObjectIdField(primary_key=True)  # Use MongoDB's native ObjectId

    # Fields that map to columns/properties in the MongoDB collection
    first_name = models.CharField(max_length=100)      # First name of account holder
    last_name = models.CharField(max_length=100)       # Last name of account holder
    email = models.EmailField(max_length=100)          # Email address (with validation)
    savings_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)  # Account balance starts at 0

    # Meta options for the model
    class Meta:
        db_table = "savings"  # Specifies the table name in MongoDB as savings
        
    # String representation of a Savings object for admin interface and debugging
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
