import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.main import app
from api.database import Base, get_db # Import your models here 
from api.utils import InputData, has_access



# Create an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# Create the database schema
Base.metadata.create_all(bind=engine)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency to use the test database
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Fixture for the database session
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    """Create a new database session for a test."""
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()



client = TestClient(app)

# Mock the has_access dependency to always return True for tests
def mock_has_access():
    return True

# Override the dependency in the FastAPI app for testing
app.dependency_overrides[has_access] = mock_has_access

@pytest.fixture(scope="module")
def setup():
    # You can add setup code here if needed
    yield
    # You can add teardown code here if needed

def test_predict_endpoint(setup,db_session):
    input_data = {
        "etat_de_route": "clear",
        "carburant": "gas",
        "turbo": "yes",
        "nombre_portes": "four",
        "type_vehicule": "sedan",
        "roues_motrices": "fwd",
        "emplacement_moteur": "front",
        "empattement": 88.6,
        "longueur": 168.8,
        "largeur": 64.1,
        "hauteur": 48.8,
        "poids_vehicule": 2548,
        "type_moteur": "dohc",
        "nombre_cylindres": "four",
        "taille_moteur": 130,
        "systeme_carburant": "mpfi",
        "taux_alésage": 3.47,
        "course": 2.68,
        "taux_compression": 9.0,
        "chevaux": 111,
        "tour_moteur": 5000,
        "consommation_ville": 21.0,
        "consommation_autoroute": 27.0,
        "marque": "toyota",
        "modèle": "corolla"
    }

    response = client.post("/predict/", json=input_data)
    assert response.status_code == 200
    json_response = response.json()
    assert "prediction" in json_response
    assert isinstance(json_response["prediction"], float)
