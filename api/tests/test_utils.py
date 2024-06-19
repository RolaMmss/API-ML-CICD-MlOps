# test_utils.py
import pytest
import os
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from pydantic import BaseModel
from unittest.mock import patch, MagicMock
from jose import jwt
from api.utils import has_access, predict_single, get_model, generate_token, InputData

# Define a fixture for the environment variables
@pytest.fixture(scope="module", autouse=True)
def load_env():
    os.environ["SECRET_KEY"] = "test_secret_key"

# Mocking InputData
class MockInputData(BaseModel):
    etat_de_route: str = "Clear"
    carburant: str = "Gasoline"
    turbo: str = "Yes"
    nombre_portes: str = "Four"
    type_vehicule: str = "Sedan"
    roues_motrices: str = "FWD"
    emplacement_moteur: str = "Front"
    empattement: float = 100.0
    longueur: float = 150.0
    largeur: float = 60.0
    hauteur: float = 55.0
    poids_vehicule: int = 2500
    type_moteur: str = "I4"
    nombre_cylindres: str = "4"
    taille_moteur: float = 130.0
    systeme_carburant: str = "MPFI"
    taux_alésage: float = 3.47
    course: float = 2.68
    taux_compression: float = 10.0
    chevaux: int = 110
    tour_moteur: int = 5000
    consommation_ville: float = 25.0
    consommation_autoroute: float = 30.0
    marque: str = "Toyota"
    modèle: str = "Camry"

@pytest.mark.asyncio
async def test_has_access():
    token = generate_token("admin")
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)
    
    result = await has_access(credentials)
    assert result == True

@pytest.mark.asyncio
async def test_has_access_invalid():
    token = generate_token("user")
    credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)
    
    with pytest.raises(HTTPException):
        await has_access(credentials)

def test_predict_single():
    model = MagicMock()
    model.predict.return_value = [15000.0]
    
    input_data = MockInputData()
    prediction = predict_single(model, input_data)
    
    assert prediction == 15000.0

@patch("builtins.open", new_callable=MagicMock)
@patch("pickle.load", return_value=MagicMock())
def test_get_model(mock_pickle_load, mock_open):
    model = get_model()
    
    mock_open.assert_called_once_with('./model/random_forest_model.pkl', 'rb')
    mock_pickle_load.assert_called_once()
    assert model == mock_pickle_load.return_value

def test_generate_token():
    token = generate_token("admin")
    payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=["HS256"])
    
    assert payload.get("sub") == "admin"
