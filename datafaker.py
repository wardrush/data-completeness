#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 12:53:42 2024

@author: wardrushton
"""
from faker import Faker
import pandas as pd
from datetime import datetime

# Initialize Faker instance
fake = Faker()

# Define a function to create a transaction history
def create_transaction_history(num=3):
    """
    Creates a list of tuples with transaction ID and datetime of purchase.
    By default, generates 5 transactions per customer.
    """
    return [(fake.uuid4(), fake.date_this_decade()) for _ in range(num)]

# Generate the database
data = {
    'FirstName': [fake.first_name() for _ in range(100)],
    'LastName': [fake.last_name() for _ in range(100)],
    'EmailAddress': [fake.email() for _ in range(100)],
    'ShippingAddress': [fake.address() for _ in range(100)],
    'PhoneNumber': [fake.phone_number() for _ in range(100)],
    'TransactionHistory': [create_transaction_history() for _ in range(100)]
}

# Create a pandas DataFrame
df = pd.DataFrame(data)

# Showing the first few rows of the dataframe to verify its structure and contents
df.to_csv('test.csv')
