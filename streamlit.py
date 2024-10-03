# # import streamlit as st
# # import pandas as pd
# # import pickle
# # import os
# # import sqlite3

# # # df = pd.read_csv('prix_voiture.csv')
# #  # Get the absolute path to the cars.db file located in the parent directory
# # db_path = os.path.abspath("cars.db")

# # # Connect to the existing cars.db file
# # connection = sqlite3.connect(db_path)

# # df = pd.read_sql_query("SELECT * FROM first_run_2017_CleanDataset", connection)
# # print(df)


# # connection.close()

# # with open('./model/random_forest_model.pkl', 'rb') as file:  
# #     model = pickle.load(file)
# #     # code pour importer le modele depuis un fichier avec pickle
# # ##########################################################################################

# # # Définir le style de l'application
# # st.set_page_config(
# #     page_title="Prédire le prix de ton voiture !",
# #     page_icon="🚗",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Ajouter une image d'arrière-plan
# # st.markdown(
# #     """
# #     <style>
# #     .stApp {
# #         background-image: url('https://images.pexels.com/photos/276334/pexels-photo-276334.jpeg?auto=compress&cs=tinysrgb&w=1600');
# #         background-size: cover;
# #         background-position: center center;
    
# #     }
# #     body p, h2 {
# #     color: black !important;
# #     }
# #     body h1 {
# #     color: red !important;
# #     }
# #     .stMarkdownContainer {
# #     color: white !important;;
# #     }
# #     </style>
# #     """,
# #     unsafe_allow_html=True
# # )

# # ##########################################################################################
# # st.title('Prédire le prix de ton voiture !')
# # st.header("Caractéristiques de la voiture")
# # # Définition des variables
# # col1, col2, col3, col4, col5 = st.columns(5)
# # with col1:
# #     etat_de_route = st.selectbox('Etat_de_route', df['etat_de_route'].unique())
# #     carburant = st.selectbox('Carburant', df['carburant'].unique())
# #     turbo = st.selectbox('Turbo', df['turbo'].unique())
# #     nombre_portes = st.selectbox('Nombre de portes', df['nombre_portes'].unique())
# #     type_vehicule = st.selectbox('Type de vehicule', df['type_vehicule'].unique())
# # with col2:   
# #     roues_motrices = st.selectbox('Roues de motrices', df['roues_motrices'].unique())
# #     emplacement_moteur = st.selectbox('Emplacement du moteur', df['emplacement_moteur'].unique())
# #     # empattement = st.slider('empattement', min_value=df['empattement'].min(), max_value=df['empattement'].max(), value=df['empattement'].median())
# #     empattement = st.slider('empattement', min_value=2.2, max_value=4.0, value=2.46)
# #     longueur = st.slider('Longueur',  min_value=3.5, max_value=5.3, value=4.4)
# #     largeur = st.slider('Largeur',  min_value=1.5, max_value=1.84, value=1.66)
# # with col3:
# #     hauteur = st.slider('Hauteur',  min_value=1.2, max_value=1.52, value=1.37)
# #     poids_vehicule = st.slider('Poids_vehicule',  min_value=674.94, max_value=1844.305, value=1097.69)
# #     type_moteur = st.selectbox('Type de moteur', df['type_moteur'].unique())
# #     nombre_cylindres = st.selectbox('Nombre de cylindres', df['nombre_cylindres'].unique())
# #     taille_moteur = st.slider('Taille_moteur',  min_value=0.99, max_value=5.342, value=1.96)
# # with col4:
# #     systeme_carburant = st.selectbox('Systeme_carburant', df['systeme_carburant'].unique())
# #     taux_alésage = st.slider('Taux_alésage',  min_value=64.51, max_value=100.076, value=84.074)
# #     course = st.slider('Course',  min_value=52.57, max_value=105.918, value=83.566)
# #     taux_compression = st.slider('Taux_compression',  min_value=7, max_value=23, value=9)
# #     chevaux = st.slider('Chevaux',  min_value=48, max_value=288, value=95)
    
# # with col5:
# #     tour_moteur = st.slider('Tour_moteur',  min_value=4150, max_value=6600, value=5200)
# #     consommation_ville = st.slider('Consommation_ville',  min_value=4.8, max_value=18.093385, value=9.800583)
# #     consommation_autoroute =  st.slider('Consommation_autoroute',  min_value=4.355815, max_value=14.700875, value=7.840467)
# #     marque = st.selectbox('Marque', df['marque'].unique())
# #     modèle = st.selectbox('Modèle', df['modèle'].unique())
    
    
# # # add a button to trigger prediction
# # if st.button('Prédire '):
# #     # create a dictionary with user inputs
# #     input_data = {
# #         'etat_de_route': etat_de_route,
# #         'carburant': carburant,
# #         'turbo': turbo,
# #         'nombre_portes': nombre_portes,
# #         'type_vehicule': type_vehicule,
# #         'roues_motrices': roues_motrices,
# #         'emplacement_moteur': emplacement_moteur,
# #         'empattement': empattement,
# #         'longueur': longueur,
# #         'largeur': largeur,
# #         'hauteur': hauteur,
# #         'poids_vehicule': poids_vehicule,
# #         'type_moteur': type_moteur,
# #         'nombre_cylindres': nombre_cylindres,
# #         'taille_moteur': taille_moteur,
# #         'systeme_carburant': systeme_carburant,
# #         'taux_alésage': taux_alésage,
# #         'course': course,
# #         'taux_compression': taux_compression,
# #         'chevaux': chevaux,
# #         'tour_moteur': tour_moteur,
# #         'consommation_ville': consommation_ville,
# #         'consommation_autoroute': consommation_autoroute,
# #         'marque': marque,
# #         'modèle': modèle,
# #     }
    
# #     # convert the dictionary to a dataframe
# #     input_df = pd.DataFrame([input_data])
    
# #     # use the pre-trained model to predict the price
# #     predicted_price = model.predict(input_df)[0]
    
# #     # show the predicted price on the app
# #     if predicted_price>0:
# #          st.info(f'Prix: {predicted_price:.2f} $')
# #     else:
# #         st.info('The trained data is not reasonable.')





# import requests
# import streamlit as st
# import pandas as pd
# import os
# # import sqlite3
# import pyodbc
# from dotenv import load_dotenv


# # # Get the absolute path to the cars.db file located in the parent directory (before deployment)
# # db_path = os.path.abspath("cars.db")

# # # Connect to the existing cars.db file
# # connection = sqlite3.connect(db_path)

# # Load environment variables from .env file
# load_dotenv()
#  # For production, we need azure sql database
# # Get connection string from environment variable
# connection_string = os.getenv("DATABASE_URL")
# connection = pyodbc.connect(connection_string)

# df = pd.read_sql_query("SELECT * FROM first_run_2017_CleanDataset", connection)
# # df = pd.read_sql_query("SELECT * FROM CarPredictions", connection)


# connection.close()

# # URL de ton API FastAPI déployée
# # API_URL = "http://localhost:8000/predict/"  # Remplace par l'URL de ton API en production si nécessaire
# API_URL = "http://20.19.201.109:8000/predict/"
# # Get the authentication token from the environment variables
# token = os.getenv("token")

# # Print the token to check if it's loaded correctly
# # print(f"Your Auth Token is: {token}")
# ##########################################################################################
# # Définir le style de l'application
# st.set_page_config(
#     page_title="Prédire le prix de ton voiture !",
#     page_icon="🚗",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Ajouter une image d'arrière-plan
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://images.pexels.com/photos/276334/pexels-photo-276334.jpeg?auto=compress&cs=tinysrgb&w=1600');
#         background-size: cover;
#         background-position: center center;
#     }
#     body p, h2 {
#         color: black !important;
#     }
#     body h1 {
#         color: red !important;
#     }
#     .stMarkdownContainer {
#         color: white !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# ##########################################################################################
# st.title('Prédire le prix de ton voiture !')
# st.header("Caractéristiques de la voiture")

# # Définition des variables
# col1, col2, col3, col4, col5 = st.columns(5)
# with col1:
#     etat_de_route = st.selectbox('Etat_de_route', df['etat_de_route'].unique())
#     carburant = st.selectbox('Carburant', df['carburant'].unique())
#     turbo = st.selectbox('Turbo', df['turbo'].unique())
#     nombre_portes = st.selectbox('Nombre de portes', df['nombre_portes'].unique())
#     type_vehicule = st.selectbox('Type de vehicule', df['type_vehicule'].unique())
# with col2:
#     roues_motrices = st.selectbox('Roues de motrices', df['roues_motrices'].unique())
#     emplacement_moteur = st.selectbox('Emplacement du moteur', df['emplacement_moteur'].unique())
#     empattement = st.slider('empattement', min_value=2.2, max_value=4.0, value=2.46)
#     longueur = st.slider('Longueur', min_value=3.5, max_value=5.3, value=4.4)
#     largeur = st.slider('Largeur', min_value=1.5, max_value=1.84, value=1.66)
# with col3:
#     hauteur = st.slider('Hauteur', min_value=1.2, max_value=1.52, value=1.37)
#     poids_vehicule = st.slider('Poids_vehicule', min_value=674.94, max_value=1844.305, value=1097.69)
#     type_moteur = st.selectbox('Type de moteur', df['type_moteur'].unique())
#     nombre_cylindres = st.selectbox('Nombre de cylindres', df['nombre_cylindres'].unique())
#     taille_moteur = st.slider('Taille_moteur', min_value=0.99, max_value=5.342, value=1.96)
# with col4:
#     systeme_carburant = st.selectbox('Systeme_carburant', df['systeme_carburant'].unique())
#     taux_alésage = st.slider('Taux_alésage', min_value=64.51, max_value=100.076, value=84.074)
#     course = st.slider('Course', min_value=52.57, max_value=105.918, value=83.566)
#     taux_compression = st.slider('Taux_compression', min_value=7, max_value=23, value=9)
#     chevaux = st.slider('Chevaux', min_value=48, max_value=288, value=95)
# with col5:
#     tour_moteur = st.slider('Tour_moteur', min_value=4150, max_value=6600, value=5200)
#     consommation_ville = st.slider('Consommation_ville', min_value=4.8, max_value=18.093385, value=9.800583)
#     consommation_autoroute = st.slider('Consommation_autoroute', min_value=4.355815, max_value=14.700875, value=7.840467)
#     marque = st.selectbox('Marque', df['marque'].unique())
#     modèle = st.selectbox('Modèle', df['modèle'].unique())

# # Add a button to trigger prediction
# if st.button('Prédire'):
#     # Créer un dictionnaire avec les données d'entrée de l'utilisateur
#     input_data = {
#         'etat_de_route': str(etat_de_route),
#         'carburant': carburant,
#         'turbo': turbo,
#         'nombre_portes': nombre_portes,
#         'type_vehicule': type_vehicule,
#         'roues_motrices': roues_motrices,
#         'emplacement_moteur': emplacement_moteur,
#         'empattement': empattement,
#         'longueur': longueur,
#         'largeur': largeur,
#         'hauteur': hauteur,
#         'poids_vehicule': int(poids_vehicule),
#         'type_moteur': type_moteur,
#         'nombre_cylindres': nombre_cylindres,
#         'taille_moteur': taille_moteur,
#         'systeme_carburant': systeme_carburant,
#         'taux_alésage': taux_alésage,
#         'course': course,
#         'taux_compression': taux_compression,
#         'chevaux': chevaux,
#         'tour_moteur': tour_moteur,
#         'consommation_ville': consommation_ville,
#         'consommation_autoroute': consommation_autoroute,
#         'marque': marque,
#         'modèle': modèle,
#     }

#     # Convert the dictionary to a dataframe
#     input_df = pd.DataFrame([input_data])
    
#     # Add the token to the headers
#     headers = {
#         "Authorization": f"Bearer {token}",
#         "Content-Type": "application/json"
#     }
#     # Envoi des données à l'API FastAPI pour obtenir la prédiction
#     response = requests.post(API_URL, json=input_data, headers=headers)
#     print(f"Reponse is: {response}")
#     if response.status_code == 200:
#         predicted_price = response.json()["prediction"]
#         st.success(f'Prix prédit: {predicted_price:.2f} $')
#     else:
#         st.error(f"Erreur lors de la prédiction via l'API: {response.text}")




import requests
import streamlit as st
import pandas as pd
import os
import sqlite3
import pyodbc
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Connect to the local SQLite (for fetching data)
def connect_to_sqlite():
    db_path = os.path.abspath("cars.db")
    connection = sqlite3.connect(db_path)
    return connection

# Connect to Azure SQL (for saving predictions)
def connect_to_azure():
    connection_string = os.getenv("DATABASE_URL")
    connection = pyodbc.connect(connection_string)
    return connection

# Fetch data from SQLite database for the slider inputs
def get_data_from_sqlite():
    connection = connect_to_sqlite()
    df = pd.read_sql_query("SELECT * FROM first_run_2017_CleanDataset", connection)
    connection.close()
    return df

# Save predictions to Azure SQL
def save_prediction_to_azure(prediction_data):
    connection = connect_to_azure()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO CarPredictions (etat_de_route, carburant, turbo, nombre_portes, type_vehicule, 
    roues_motrices, emplacement_moteur, empattement, longueur, largeur, hauteur, 
    poids_vehicule, type_moteur, nombre_cylindres, taille_moteur, systeme_carburant, 
    taux_alésage, course, taux_compression, chevaux, tour_moteur, consommation_ville, 
    consommation_autoroute, marque, modèle, predicted_price)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)  -- 26 placeholders
    """

    cursor.execute(insert_query, (
        prediction_data['etat_de_route'], prediction_data['carburant'], prediction_data['turbo'],
        prediction_data['nombre_portes'], prediction_data['type_vehicule'], prediction_data['roues_motrices'],
        prediction_data['emplacement_moteur'], prediction_data['empattement'], prediction_data['longueur'],
        prediction_data['largeur'], prediction_data['hauteur'], prediction_data['poids_vehicule'],
        prediction_data['type_moteur'], prediction_data['nombre_cylindres'], prediction_data['taille_moteur'],
        prediction_data['systeme_carburant'], prediction_data['taux_alésage'], prediction_data['course'],
        prediction_data['taux_compression'], prediction_data['chevaux'], prediction_data['tour_moteur'],
        prediction_data['consommation_ville'], prediction_data['consommation_autoroute'], prediction_data['marque'],
        prediction_data['modèle'], prediction_data['predicted_price']
    ))
    
    connection.commit()
    connection.close()

# URL of your deployed FastAPI
API_URL = "http://20.19.201.109:8000/predict/"
token = os.getenv("token")

# Streamlit UI
st.set_page_config(
    page_title="Prédire le prix de ton voiture !",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add background image styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://images.pexels.com/photos/276334/pexels-photo-276334.jpeg?auto=compress&cs=tinysrgb&w=1600');
        background-size: cover;
        background-position: center center;
    }
    body p, h2 {
        color: black !important;
    }
    body h1 {
        color: red !important;
    }
    .stMarkdownContainer {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Prédire le prix de ton voiture !')
st.header("Caractéristiques de la voiture")

# Fetch data from the local SQLite database
df = get_data_from_sqlite()

# Define user input sections
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    etat_de_route = st.selectbox('Etat_de_route', df['etat_de_route'].unique())
    carburant = st.selectbox('Carburant', df['carburant'].unique())
    turbo = st.selectbox('Turbo', df['turbo'].unique())
    nombre_portes = st.selectbox('Nombre de portes', df['nombre_portes'].unique())
    type_vehicule = st.selectbox('Type de vehicule', df['type_vehicule'].unique())
with col2:
    roues_motrices = st.selectbox('Roues de motrices', df['roues_motrices'].unique())
    emplacement_moteur = st.selectbox('Emplacement du moteur', df['emplacement_moteur'].unique())
    empattement = st.slider('empattement', min_value=2.2, max_value=4.0, value=2.46)
    longueur = st.slider('Longueur', min_value=3.5, max_value=5.3, value=4.4)
    largeur = st.slider('Largeur', min_value=1.5, max_value=1.84, value=1.66)
with col3:
    hauteur = st.slider('Hauteur', min_value=1.2, max_value=1.52, value=1.37)
    poids_vehicule = st.slider('Poids_vehicule', min_value=674.94, max_value=1844.305, value=1097.69)
    type_moteur = st.selectbox('Type de moteur', df['type_moteur'].unique())
    nombre_cylindres = st.selectbox('Nombre de cylindres', df['nombre_cylindres'].unique())
    taille_moteur = st.slider('Taille_moteur', min_value=0.99, max_value=5.342, value=1.96)
with col4:
    systeme_carburant = st.selectbox('Systeme_carburant', df['systeme_carburant'].unique())
    taux_alésage = st.slider('Taux_alésage', min_value=64.51, max_value=100.076, value=84.074)
    course = st.slider('Course', min_value=52.57, max_value=105.918, value=83.566)
    taux_compression = st.slider('Taux_compression', min_value=7, max_value=23, value=9)
    chevaux = st.slider('Chevaux', min_value=48, max_value=288, value=95)
with col5:
    tour_moteur = st.slider('Tour_moteur', min_value=4150, max_value=6600, value=5200)
    consommation_ville = st.slider('Consommation_ville', min_value=4.8, max_value=18.093385, value=9.800583)
    consommation_autoroute = st.slider('Consommation_autoroute', min_value=4.355815, max_value=14.700875, value=7.840467)
    marque = st.selectbox('Marque', df['marque'].unique())
    modèle = st.selectbox('Modèle', df['modèle'].unique())

# Add a button to trigger prediction
if st.button('Prédire'):
    # Gather user input
    input_data = {
        'etat_de_route': str(etat_de_route),
        'carburant': carburant,
        'turbo': turbo,
        'nombre_portes': nombre_portes,
        'type_vehicule': type_vehicule,
        'roues_motrices': roues_motrices,
        'emplacement_moteur': emplacement_moteur,
        'empattement': empattement,
        'longueur': longueur,
        'largeur': largeur,
        'hauteur': hauteur,
        'poids_vehicule': int(poids_vehicule),
        'type_moteur': type_moteur,
        'nombre_cylindres': nombre_cylindres,
        'taille_moteur': taille_moteur,
        'systeme_carburant': systeme_carburant,
        'taux_alésage': taux_alésage,
        'course': course,
        'taux_compression': taux_compression,
        'chevaux': chevaux,
        'tour_moteur': tour_moteur,
        'consommation_ville': consommation_ville,
        'consommation_autoroute': consommation_autoroute,
        'marque': marque,
        'modèle': modèle,
    }

    # # Print input data and its types
    # print("Input Data:", input_data)
    # print("Types:", {key: type(value) for key, value in input_data.items()})

    # Add token to headers
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Send input data to FastAPI for prediction
    response = requests.post(API_URL, json=input_data, headers=headers)
        
    #     # Save prediction
    if response.status_code == 200:
        predicted_price = response.json()["prediction"]
        st.success(f'Prix prédit: {predicted_price:.2f} $')
        
        # Add predicted price to input data
        input_data['predicted_price'] = predicted_price
        
        # Save prediction to Azure SQL
        save_prediction_to_azure(input_data)
        st.info("Les données et la prédiction ont été enregistrées dans Azure SQL.")
