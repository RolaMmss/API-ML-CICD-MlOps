# API-ML-CICD-MlOps
Develop an API with token-based authentication that exposes a machine learning model including pytest quality tests and mlflow tracking on azure, and create a continuous delivery pipeline for this model in an MLOps approach to automate the steps of validation, testing, packaging, and deployment.

## Setup:
### Virtual environment and install all dependencies
- Create a virtual environment : python3 -m venv myenv
- Activate the virtual environment : source myenv/bin/activate
- Execute the requirements file to install all dependencies : pip install -r requirements.txt
### Build sqlite databases
- Create and import tables: 
    sqlite3 cars.db < database_building/create_table.sql
    sqlite3 cars.db  < database_building/import_table.sql
- Execute data_cleaning.py to get the cleaned table : first_run_2017_CleanDataset
### Modelisation and MLflow
- Execute modelisation.py
- Launch MLflow : mlflow ui
### Store your private infos in a private file
- Create .env file to save all secret info such as : 
        - DATABASE_URL=sqlite:///./cars.db
        - secret key 
        You may generate a secret key by:
        import secrets
        # Generate a random 32-byte (256-bit) key
        secret_key = secrets.token_hex(32)
        print(secret_key)
        - ALGORITHM
        - USERNAME
        - PASSWORD
### Test the API 
    - Generate a token
    -  python3 -m api.main
    - a FASTAPI Swaggge UI will open. Click on predict then on Try it out to generate a prediction. Fille the requested body for example:
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
        Then execute. You will get an error : "Not authenticated". You need to generate a token.
        Execute utils.py to generate a token, copy it, then click on Authorize.
## Run the pytests : 
PYTHONPATH=./ pytest api/tests/           ( in case it didn't find api, this will lead to the correct path)

### Deploy the API and streamlit
- Build and test the Docker Image locally: 
        - docker build -t dockerimage:latest -f api/Dockerfile .
        - docker run -p 8000:8000 dockerimage:latest
        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.
- Tag the image before pushing it to dockerhub
        - docker login
        - docker tag dockerimage repo_docker:latest
        - docker push rola123/repo_docker:latest

### Run streamlit
streamlit run streamlit.py


## Create Azure Container Instance
Execute create_ACR.sh in the terminal as follows:
    cd to the directory root next to api,model, .env, etc...
    chmod +x scripts/create_ACR.sh
    scripts/create_ACR.sh

## Test deployed api on azure
- Be sure that ACR container is running on azure.
- Get IP from ACR, open a new window and add the required port 8000.
     http://containerinstanceapi.francecentral.azurecontainer.io:8000/docs


## Azure SQL Database Creation Script

This repository contains a shell script (`create_sql_db.sh`) to automate the creation of an Azure SQL Server and an Azure SQL Database using the Azure CLI. The script configures the SQL Server and Database in a pre-existing Azure resource group, along with an optional firewall rule to allow access from all IP addresses.
### Make it executable by running:     
  chmod +x scripts/create_Azure_sql_db.sh
## Run the script:                   
  ./scripts/create_Azure_sql_db.sh

### Prerequisites

Before running this script, ensure that you have:

1. An existing **Azure Resource Group**.
2. The **Azure CLI** installed and configured on your machine. You can install it by following the official [Azure CLI installation guide](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
3. You must be logged into your Azure account using the CLI:




