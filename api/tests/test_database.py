# test_database.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Car, Prediction, generate_id, create_db_prediction

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"

# Create a new engine instance
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)

# Fixture for the database session
@pytest.fixture(scope="function")
def db_session():
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

def test_generate_id():
    """Test the generate_id utility function."""
    generated_id = generate_id()
    assert isinstance(generated_id, str)
    assert len(generated_id) == 14

def test_create_db_prediction(db_session):
    """Test creating a prediction in the database."""
    prediction_data = {
        "timestamp": "2024-06-19T12:00:00Z",
        "etat_de_route": "Clear",
        "carburant": "Gasoline",
        "turbo": "Yes",
        "nombre_portes": "Four",
        "type_vehicule": "Sedan",
        "roues_motrices": "FWD",
        "emplacement_moteur": "Front",
        "empattement": 100.0,
        "longueur": 150.0,
        "largeur": 60.0,
        "hauteur": 55.0,
        "poids_vehicule": 2500,
        "type_moteur": "I4",
        "nombre_cylindres": "4",
        "taille_moteur": 130.0,
        "systeme_carburant": "MPFI",
        "taux_alésage": 3.47,
        "course": 2.68,
        "taux_compression": 10.0,
        "chevaux": 110,
        "tour_moteur": 5000,
        "consommation_ville": 25.0,
        "consommation_autoroute": 30.0,
        "marque": "Toyota",
        "modèle": "Camry",
        "prediction": 15000.0,
        "model": "linear_regression"
    }
    
    db_prediction = create_db_prediction(prediction_data, db_session)
    assert db_prediction.prediction_id is not None
    assert db_prediction.timestamp == prediction_data["timestamp"]
    assert db_prediction.prediction == prediction_data["prediction"]
    
    # Verify the prediction is actually in the database
    retrieved_prediction = db_session.query(Prediction).filter_by(prediction_id=db_prediction.prediction_id).first()
    assert retrieved_prediction is not None
    assert retrieved_prediction.timestamp == prediction_data["timestamp"]

def test_car_model(db_session):
    """Test the Car model."""
    car_data = {
        "car_ID": 1,
        "symboling": 3,
        "CarName": "alfa-romero giulia",
        "fueltype": "gas",
        "aspiration": "std",
        "doornumber": "two",
        "carbody": "convertible",
        "drivewheel": "rwd",
        "enginelocation": "front",
        "wheelbase": 88.6,
        "carlength": 168.8,
        "carwidth": 64.1,
        "carheight": 48.8,
        "curbweight": 2548,
        "enginetype": "dohc",
        "cylindernumber": "four",
        "enginesize": 130,
        "fuelsystem": "mpfi",
        "boreratio": 3.47,
        "stroke": 2.68,
        "compressionratio": 9.0,
        "horsepower": 111,
        "peakrpm": 5000,
        "citympg": 21,
        "highwaympg": 27,
        "price": 13495
    }
    
    new_car = Car(**car_data)
    db_session.add(new_car)
    db_session.commit()
    
    retrieved_car = db_session.query(Car).filter_by(car_ID=car_data["car_ID"]).first()
    assert retrieved_car is not None
    assert retrieved_car.CarName == car_data["CarName"]
