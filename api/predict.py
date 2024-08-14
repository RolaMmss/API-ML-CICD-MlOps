# predict.py
# FastAPI route for making predictions
# This file defines the prediction endpoint using FastAPI, leveraging the utilities and database models defined in database.py and utils.py.
# It sets up the API router and the logic for handling prediction requests and saving results to the database.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.utils import has_access, InputData, predict_single, get_model
from api.database import get_db, create_db_prediction
import time

router = APIRouter()

@router.post("/", response_model=dict)
def predict(
    input_data: InputData,
    authenticated: bool = Depends(has_access),
    db: Session = Depends(get_db)
) -> dict:
    model = get_model()
    prediction = predict_single(model, input_data)

    # MLOps: Save predictions to database
    prediction_dict = {
        "prediction": prediction,
        "etat_de_route": input_data.etat_de_route,
        "carburant": input_data.carburant,
        "turbo": input_data.turbo,
        "nombre_portes": input_data.nombre_portes,
        "type_vehicule": input_data.type_vehicule,
        "roues_motrices": input_data.roues_motrices,
        "emplacement_moteur": input_data.emplacement_moteur,
        "empattement": input_data.empattement,
        "longueur": input_data.longueur,
        "largeur": input_data.largeur,
        "hauteur": input_data.hauteur,
        "poids_vehicule": input_data.poids_vehicule,
        "type_moteur": input_data.type_moteur,
        "nombre_cylindres": input_data.nombre_cylindres,
        "taille_moteur": input_data.taille_moteur,
        "systeme_carburant": input_data.systeme_carburant,
        "taux_alésage": input_data.taux_alésage,
        "course": input_data.course,
        "taux_compression": input_data.taux_compression,
        "chevaux": input_data.chevaux,
        "tour_moteur": input_data.tour_moteur,
        "consommation_ville": input_data.consommation_ville,
        "consommation_autoroute": input_data.consommation_autoroute,
        "marque": input_data.marque,
        "modèle": input_data.modèle,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "model": "random_forest_model"
    }
    create_db_prediction(prediction_dict, db)

    return {"prediction": prediction}
