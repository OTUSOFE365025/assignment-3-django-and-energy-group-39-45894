############################################################################
## Django ORM Standalone Python Template
############################################################################
""" Here we'll import the parts of Django we need. It's recommended to leave
these settings as is, and skip to START OF APPLICATION section below """

# Turn off bytecode generation
import sys
sys.dont_write_bytecode = True

# Import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# setup django environment
import django
django.setup()

# Import your models for use in your script
from db.models import *

############################################################################
## START OF APPLICATION
############################################################################
""" Replace the code below with your own """

#Delete all existing products
Product.objects.all().delete()

# Seed a few sample products in the database
Product.objects.create(upc='123456789012', name='Milk', price=2.99)
Product.objects.create(upc='987654321098', name='Bread', price=1.99)
Product.objects.create(upc='555666777888', name='Eggs', price=3.49)
Product.objects.create(upc='222333444555', name='Cheese', price=5.25)

#Simulate Scanning Products by UPC
while True:
    upc = input("Enter or scan product UPC or type 'exit' to quit (132456798012 - example upc): ").strip()
    if upc.lower() == 'exit':
        print("Exiting Cash Register")
        break

    try:
        product = Product.objects.get(upc=upc)
        print(f"Product Found: {product.name} - ${product.price}\n")
    except Product.DoesNotExist:
        print("Product not found. Please try again.\n")