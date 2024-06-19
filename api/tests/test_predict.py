import pytest
from fastapi.testclient import TestClient
from fastapi import Depends
from api.main import app
from api.utils import InputData, has_access

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

def test_predict_endpoint(setup):
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
