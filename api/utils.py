# This file will contain utility functions, including access control, model loading, and token generation.
# These utilities will be used by other parts of the application, such as the prediction endpoint and main application setup.
# utils.py script
from fastapi import HTTPException, status, Depends
from jose import JWTError, jwt
import os
from pydantic import BaseModel
import pickle
import pandas as pd
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Define a Pydantic model to validate the request body
class InputData(BaseModel):
    etat_de_route: str
    carburant: str
    turbo: str
    nombre_portes: str
    type_vehicule: str
    roues_motrices: str
    emplacement_moteur: str
    empattement: float
    longueur: float
    largeur: float
    hauteur: float
    poids_vehicule: int
    type_moteur: str
    nombre_cylindres: str
    taille_moteur: float
    systeme_carburant: str
    taux_alésage: float
    course: float
    taux_compression: float
    chevaux: int
    tour_moteur: int
    consommation_ville: float
    consommation_autoroute: float
    marque: str
    modèle: str

async def has_access(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())):
    token = credentials.credentials
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = "HS256"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
    except JWTError:
        raise credentials_exception
    if username == "admin":
        return True
    else:
        raise credentials_exception


def predict_single(model, input_data: InputData):
    input_df = pd.DataFrame([input_data.dict()])
    prediction = model.predict(input_df)
    return prediction[0]

def get_model():
    with open('./model/random_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def generate_token(to_encode):
    load_dotenv()
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = "HS256"
    to_encode_dict = {"sub": to_encode}
    encoded_jwt = jwt.encode(to_encode_dict, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

if __name__ == "__main__":
    print(generate_token("admin"))
    
    
    
 