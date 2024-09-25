import mlflow
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sqlite3
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the trained model
with open("random_forest_model.pkl", "rb") as file:
    model = pickle.load(file)

# Step 1: Calculate predictions for the training data
# Connect to the existing cars.db file
db_path = os.path.abspath("cars.db")
connection = sqlite3.connect(db_path)

# Fetch the data for training
df = pd.read_sql_query("SELECT * FROM first_run_2017_CleanDataset", connection)
X = df.drop(['prix'], axis=1)
y = df['prix']
X_train, _, y_train, _ = train_test_split(X, y, train_size=0.8, random_state=42)

# Make predictions on the training data
local_predictions = model.predict(X_train)

# Step 2: Fetch production predictions from Azure SQL
# Connect to Azure SQL Database (Make sure to replace with your connection details)
import pyodbc

azure_conn_string = (
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=tcp:db-sql-server-rola.database.windows.net,1433;"
    "Database=azure-db-sql;"
    "Uid=rola;"
    "Pwd=your_password;"  # Replace with your actual password
)

azure_connection = pyodbc.connect(azure_conn_string)
production_df = pd.read_sql_query("SELECT predicted_price FROM CarPredictions", azure_connection)
production_predictions = production_df['predicted_price'].values

# Close the connections
connection.close()
azure_connection.close()

# Step 3: Prepare data for the bar plot
mean_local_prediction = np.mean(local_predictions)
mean_production_prediction = np.mean(production_predictions)

labels = ['Local Predictions (Training)', 'Production Predictions']
mean_values = [mean_local_prediction, mean_production_prediction]

# Create a bar plot to compare the average predictions
plt.figure(figsize=(8, 6))
plt.bar(labels, mean_values, color=['blue', 'orange'])
plt.title('Comparison of Mean Predictions: Training vs Production')
plt.ylabel('Mean Predicted Price')
plt.ylim([0, max(mean_values) + 1000])  # Adjust the y-axis limit as needed
plt.axhline(y=0, color='black', linewidth=0.8)  # Add a baseline for reference
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better readability

# Show the plot
plt.show()
