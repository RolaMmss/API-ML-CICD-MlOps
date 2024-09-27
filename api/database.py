# database.py
# This file sets up the database connection, defines the data models (Car and Prediction), and includes utility functions (generate_id, create_db_prediction) and the session management dependency (get_db).
# It's essential to define the database schema and connection details first because other parts of the application will depend on these models and utilities.

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from dotenv import load_dotenv
import os
import string
import random

# Environment Variables: We use load_dotenv() to load the database URL from the .env file.
load_dotenv()

# DATABASE_URL = os.environ.get("DATABASE_URL")  # production
DATABASE_URL = "sqlite:///./cars.db"  # local
# Connect to the SQLite database specified in the .env file.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# Session Management: SessionLocal provides session management for the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base Model: Base is the declarative base class for SQLAlchemy models.
Base = declarative_base()

# Cars Model: The Car class defines the schema for the Cars table.
# Define the Cars table:
class Car(Base):
    __tablename__ = "Cars"
    
    car_ID = Column(Integer, primary_key=True, index=True)
    symboling = Column(Integer)
    CarName = Column(String)
    fueltype = Column(String)
    aspiration = Column(String)
    doornumber = Column(String)
    carbody = Column(String)
    drivewheel = Column(String)
    enginelocation = Column(String)
    wheelbase = Column(Float)
    carlength = Column(Float)
    carwidth = Column(Float)
    carheight = Column(Float)
    curbweight = Column(Integer)
    enginetype = Column(String)
    cylindernumber = Column(String)
    enginesize = Column(Integer)
    fuelsystem = Column(String)
    boreratio = Column(Float)
    stroke = Column(Float)
    compressionratio = Column(Float)
    horsepower = Column(Integer)
    peakrpm = Column(Integer)
    citympg = Column(Integer)
    highwaympg = Column(Integer)
    price = Column(Integer)

# Predictions Model: The Prediction class defines the schema for the predictions table.
# Define the Predictions table
class Prediction(Base):
    __tablename__ = "predictions"

    prediction_id = Column(String, primary_key=True, index=True)
    timestamp = Column(String)
    etat_de_route = Column(Integer)
    carburant = Column(String)
    turbo = Column(String)
    nombre_portes = Column(String)
    type_vehicule = Column(String)
    roues_motrices = Column(String)
    emplacement_moteur = Column(String)
    empattement = Column(Float)
    longueur = Column(Float)
    largeur = Column(Float)
    hauteur = Column(Float)
    poids_vehicule = Column(Float)
    type_moteur = Column(String)
    nombre_cylindres = Column(String)
    taille_moteur = Column(Float)
    systeme_carburant = Column(String)
    taux_alésage = Column(Float)
    course = Column(Float)
    taux_compression = Column(Float)
    chevaux = Column(Integer)
    tour_moteur = Column(Integer)
    consommation_ville = Column(Float)
    consommation_autoroute = Column(Float)
    marque = Column(String)
    modèle = Column(String)
    prediction = Column(Float)
    model = Column(String)

# Session Dependency: get_db provides a database session for FastAPI dependencies.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility Functions: generate_id generates a unique ID, and create_db_prediction saves a prediction to the database.
def generate_id():
    """Generate a unique string ID."""
    length = 14
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

def create_db_prediction(prediction: dict, db: Session) -> Prediction:
    db_prediction = Prediction(**prediction, prediction_id=generate_id())
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    return db_prediction

# Create Tables: Base.metadata.create_all(bind=engine) creates the tables in the database if they don't already exist.
if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)


