<<<<<<< HEAD
# API-ML-CICD-MlOps
Develop an API that exposes an artificial intelligence model, monitor this model, integrate the API into an application, program automated tests for this model, and create a continuous delivery pipeline for this AI model in an MLOps approach to automate the steps of validation, testing, packaging, and deployment of the model.
=======
# API-ML-CICD-MlOps# 
Développer une API exposant un modèle d’intelligence artificielle, monitorer ce modèle, intégrer l’API dans une application, programmer les tests automatisés de ce modèle, créer une chaîne de livraison continue de ce modèle d'IA dans une approche MLOps pour automatiser les étapes de validation, de test, de packaging* et de déploiement du modèle.
>>>>>>> 546955c1 (mod readme)

## Building a Car Price Estimation Application

Your client, a car dealer, wants the creation of an application that can estimate the price of a car.

### Definitions:

    car_ID: Unique identifier for each car in the dataset.
    symboling: Insurance risk rating of the car, where -2 is the most risky and +3 is the least risky.
    CarName: The name of the car, including both the brand and model.
    fueltype: The type of fuel used by the car (either "essence" or "diesel").
    aspiration: Whether the car is naturally aspirated or turbocharged.
    doornumber: The number of doors on the car (either "deux" or "quatre").
    carbody: The body style of the car (e.g., sedan, hatchback, convertible, etc.).
    drivewheel: The type of transmission used by the car (e.g., front-wheel drive, rear-wheel drive, all-wheel drive).
    enginelocation: The location of the engine (either "avant" or "arrière").
    wheelbase: The distance between the front and rear wheels of the car.
    carlength: The total length of the car.
    carwidth: The total width of the car.
    carheight: The total height of the car.
    curbweight: The weight of the car without any occupants or cargo.
    enginetype: The type of engine used by the car (e.g., four cylinders, six cylinders, rotary, etc.).
    cylindernumber: The number of cylinders in the car's engine.
    enginesize: The size of the car's engine in cubic centimeters (cc).
    fuelsystem: The type of fuel system used by the car (e.g., carbureted, fuel injected).
    boreratio: The ratio of the diameter of the engine cylinders to their length.
    stroke: The distance traveled by the piston up and down in the engine cylinders.
    compressionratio: The ratio of the volume of the engine's combustion chamber when the piston is at the bottom of its stroke compared to when it is at the top.
    horsepower: The power of the car's engine in horsepower (hp).
    peakrpm: The engine speed at which the car's maximum power is produced.
    citympg: The car's fuel economy in miles per gallon (mpg) under city driving conditions.
    highwaympg: The car's fuel economy in miles per gallon (mpg) under highway driving conditions.
    price: The manufacturer's suggested retail price (MSRP) of the car in US dollars.

Conversions:

    empattement: in meters (1 inch = 0.0254 meters)
    longueur: in meters
    largeur: in meters
    hauteur: in meters
    poids_vehicule: in kilograms (1 pound = 0.453592 kilograms)
    taille_moteur: in liters (1 cubic inch = 0.0163871 liters)
    taux_alésage: in millimeters (1 inch = 25.4 millimeters)
    course: in millimeters
    taux_compression: ratio (no conversion needed)
    tour_moteur: in revolutions per minute (no conversion needed)
    consommation_ville: in liters per 100 kilometers (1 mile per gallon = 0.425 kilometers per liter)
    consommation_autoroute: in liters per 100 kilometers

## Steps:
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
        - secret key . You may generate a secret key by:
                import secrets
                # Generate a random 32-byte (256-bit) key
                secret_key = secrets.token_hex(32)
                print(secret_key)
        - ALGORITHM
        - USERNAME
        - PASSWORD
## Test the API 
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
     http://98.66.198.165:8000/docs


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




