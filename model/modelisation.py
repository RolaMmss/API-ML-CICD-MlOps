import mlflow
import mlflow.sklearn
import sqlite3
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PolynomialFeatures
from sklearn.ensemble import RandomForestRegressor
import pickle

 # Get the absolute path to the cars.db file located in the parent directory
db_path = os.path.abspath("cars.db")

# Connect to the existing cars.db file
connection = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM first_run_2017_CleanDataset", connection)
print(df)


connection.close()

run_name = "experiment_1_run_1"

# Define your data preprocessing and model training steps
y = df['prix']
X = df.drop(['prix'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

categorical_features = ['etat_de_route', 'carburant', 'turbo', 'nombre_portes', 'type_vehicule', 'roues_motrices', 'emplacement_moteur', 'type_moteur', 'nombre_cylindres', 'systeme_carburant', 'marque', 'modèle']
numeric_features = ['empattement', 'longueur', 'largeur', 'hauteur', 'poids_vehicule', 'taille_moteur', 'taux_alésage', 'course', 'taux_compression', 'chevaux', 'tour_moteur', 'consommation_ville', 'consommation_autoroute']

categorical_transformer = Pipeline(steps=[
    ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))
])

numeric_transformer = Pipeline([
    ('min_max', MinMaxScaler()),
    ('poly', PolynomialFeatures(degree=2, include_bias=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, numeric_features),
    ('cat', categorical_transformer, categorical_features)
])

# Set up MLflow experiment
experiment_name = "predict_price" if run_name != "test_run" else "test_experiment"
experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment is None:
    experiment_id = mlflow.create_experiment(experiment_name)
else:
    experiment_id = experiment.experiment_id

# Start MLflow run
with mlflow.start_run(experiment_id=experiment_id, run_name=run_name) as run:
    # Define the model pipeline
    model = Pipeline([
        ('preprocess', preprocessor),
        ('random_forest', RandomForestRegressor(n_estimators=50, max_depth=20, min_samples_split=2, min_samples_leaf=1, random_state=42))
    ])
    
    # Log model parameters
    mlflow.log_param("n_estimators", 50)
    mlflow.log_param("max_depth", 20)
    mlflow.log_param("min_samples_split", 2)
    mlflow.log_param("min_samples_leaf", 1)
    mlflow.log_param("random_state", 42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Log model
    mlflow.sklearn.log_model(model, "random_forest_model")
    
    # Calculate and log model metrics
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    mlflow.log_metric("train_score", train_score)
    mlflow.log_metric("test_score", test_score)

# End MLflow run
mlflow.end_run()

# Save the model using pickle for FastAPI
with open("random_forest_model.pkl", "wb") as file:
    pickle.dump(model, file)


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, PolynomialFeatures
# from sklearn.compose import ColumnTransformer
# import mlflow
# import mlflow.sklearn

# mlflow.set_tracking_uri("http://localhost:5000")
# experiment_name = "realiser_car_price_prediction"

# # Check if the experiment already exists, if not, create it
# experiment = mlflow.get_experiment_by_name(experiment_name)
# if experiment is None:
#     print(f"Creating experiment: {experiment_name}")
#     experiment_id = mlflow.create_experiment(experiment_name)
# else:
#     experiment_id = experiment.experiment_id
#     print(f"Using existing experiment: {experiment_name} with ID {experiment_id}")


# # Load data
# df = pd.read_csv('data/prix_voiture.csv')


# # Define X and y variables
# y = df['prix']
# X = df[['taille_moteur', 'poids_vehicule', 'chevaux', 'consommation_autoroute', 'consommation_ville', 'largeur', 'longueur', 'roues_motrices', 'empattement', 'systeme_carburant', 'turbo', 'marque', 'etat_de_route', 'type_vehicule', 'emplacement_moteur', 'type_moteur', 'nombre_cylindres']]

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42)

# # Define transformers
# categorical_features = ['etat_de_route', 'turbo', 'type_vehicule', 'roues_motrices', 'emplacement_moteur', 'type_moteur', 'nombre_cylindres', 'systeme_carburant', 'marque']
# numeric_features = ['empattement', 'longueur', 'largeur', 'poids_vehicule', 'taille_moteur', 'chevaux', 'consommation_ville', 'consommation_autoroute']

# categorical_transformer = Pipeline(steps=[
#     ('onehotencoder', OneHotEncoder(handle_unknown='ignore'))
# ])
# numeric_transformer = Pipeline([
#     ('min_max', MinMaxScaler()),
#     ('poly', PolynomialFeatures(degree=2, include_bias=False))
# ])

# preprocessor = ColumnTransformer(transformers=[
#     ('num', numeric_transformer, numeric_features),
#     ('cat', categorical_transformer, categorical_features)
# ])

# # Define model
# rf_model = Pipeline([
#     ('preprocess', preprocessor),
#     ('random_forest', RandomForestRegressor(n_estimators=15, max_depth=20, min_samples_split=2, min_samples_leaf=1, random_state=42))
# ])

# # Start MLflow run
# with mlflow.start_run(experiment_id=experiment_id, run_name="initial_run") as run:
#     print(f"Running experiment with ID {run.info.experiment_id} and run ID {run.info.run_id}")
    

#     # Train the model
#     rf_model.fit(X_train, y_train)

#     # Predict on the test data
#     y_pred = rf_model.predict(X_test)

#     # Calculate the R^2 score on the test data
#     score = rf_model.score(X_test, y_test)

#     # Log parameters
#     mlflow.log_param("n_estimators", 15)
#     mlflow.log_param("max_depth", 20)

#     # Log metrics
#     mlflow.log_metric("R2 score", score)

#     # Log model
#     mlflow.sklearn.log_model(rf_model, "random_forest_model")
#     print("MLflow run complete. Check the MLflow UI for experiment details.")

# # To start mlflow : mlflow ui