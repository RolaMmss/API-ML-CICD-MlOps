#create_table_azure.py
# run: python create_table_azure.py
import os
from dotenv import load_dotenv
import pyodbc

# Load environment variables from .env file
load_dotenv()

# Get connection string from environment variable
connection_string = os.getenv("DATABASE_URL")

# Establish a connection
connection = pyodbc.connect(connection_string)

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Read the SQL script from the file
with open('database_building/create_table_azure.sql', 'r') as file:
    sql_script = file.read()

# Execute the SQL script
cursor.execute(sql_script)

# Commit the changes and close the connection
connection.commit()
cursor.close()
connection.close()

print("Table 'Cars' created successfully!")
