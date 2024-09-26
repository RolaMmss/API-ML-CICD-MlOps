# API-ML-CICD-MlOps
## Purpose
The objective of this project is to develop an API that exposes an artificial intelligence model, monitor this model, integrate the API into an application, program automated tests for this model, and create a continuous delivery pipeline for this AI model in an MLOps approach to automate the steps of validation, testing, packaging, and deployment of the model.

It includes:

  - A machine learning model and mlflow tracking on azure
  - A deployed API (FastAPI) on Azure with token-based authentication and Ml-ops Monitoring 
  - A Streamlit which serves as user interface
  - The procedure for building an SQL database on Azure to save predictions on production

## Setup:
1. Create/activate a virtual environement and install requirements:

  - python -m venv myenv
  - source myenv/bin/activate
  - pip install -r requirements.txt
2. Create .env file in the root directory to save secret information such as token of the API

3. Execute these commands to build sqlite databases

    sqlite3 cars.db < database_building/create_table.sql
    sqlite3 cars.db  < database_building/import_table.sql
4. Execute data_cleaning.py to get the cleaned table first_run_2017_CleanDataset

5. Modelisation and MLflow

  - Execute modelisation.py 
  - Launch MLflow : mlflow ui


## Launch the API
1. Execute the command to test the API 
    python -m api.main
2. Add /docs to the url
    http://0.0.0.0:8000/docs
  - a FASTAPI Swaggge UI will open. Click on predict then on Try it out to generate a prediction. Fill the requested body for example:

    {"etat_de_route": "1",
    "carburant": "essence",
    "turbo": "turbo",
    "nombre_portes": "quatre",
    "type_vehicule": "berline",
    "roues_motrices": "traction",
    "emplacement_moteur": "avant",
    "empattement": 2.69,
    "longueur": 4.89,
    "largeur": 1.81,
    "hauteur": 1.41,
    "poids_vehicule": 1400,
    "type_moteur": "ohc",
    "nombre_cylindres": "five",
    "taille_moteur": 2,
    "systeme_carburant": "mpfi",
    "taux_alésage": 79,
    "course": 86.36,
    "taux_compression": 8,
    "chevaux": 140,
    "tour_moteur": 5500,
    "consommation_ville": 13,
    "consommation_autoroute": 11,
    "marque": "audi",
    "modèle": "4000"
  }

  Then execute. You will get an error : "Not authenticated". 
  
  You need to submit a token.

  Execute utils.py to generate a token, copy it, then click on Authorize.

## Run the pytests : 
  - pytest
  - PYTHONPATH=./ pytest api/tests/           ( in case it didn't find api, this will lead to the correct path)

## Deploy the API
  - Build and test the Docker Image locally: 

    - docker build -t dockerimage:latest -f api/Dockerfile .

    - docker run -p 8000:8000 dockerimage:latest

    - then /docs

    Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.

  - Tag the image before pushing it to dockerhub
    - docker login
    - docker tag dockerimage repo_docker:latest
    - docker push rola123/repo_docker:latest

## Run streamlit for the deployed api
streamlit run streamlit.py

# Remarks:
## To create Azure Container Instance
Execute create_ACR.sh in the terminal as follows:

  cd to the directory root next to api,model, .env, etc...

  chmod +x scripts/create_ACR.sh

  scripts/create_ACR.sh

## To test the deployed api on azure
- Be sure that ACR container is running on azure.
- Get IP from ACR, open a new window and add the required port 8000.
     http://20.19.201.109:8000/docs/


## Azure SQL Database Creation Script

This repository contains a shell script (`create_sql_db.sh`) to automate the creation of an Azure SQL Server and an Azure SQL Database using the Azure CLI. The script configures the SQL Server and Database in a pre-existing Azure resource group, along with an optional firewall rule to allow access from all IP addresses.
### Make it executable by running:     
  chmod +x scripts/create_Azure_sql_db.sh
### Run the script:                   
  ./scripts/create_Azure_sql_db.sh

### Prerequisites

Before running this script, ensure that you have:

1. An existing **Azure Resource Group**.
2. The **Azure CLI** installed and configured on your machine. You can install it by following the official [Azure CLI installation guide](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
3. You must be logged into your Azure account using the CLI


