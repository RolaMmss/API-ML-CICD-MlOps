# API-ML-CICD-MlOps# 

# Building a Car Price Estimation Application

Your client, a car dealer, wants the creation of an application that can estimate the price of a car.

# Definitions:

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

# Steps:
## Virtual environment and install all dependencies
- Create a virtual environment : python3 -m venv myenv
- Activate the virtual environment : source myenv/bin/activate
- Execute the requirements file to install all dependencies : pip install -r requirements.txt
## Build sqlite databases
- Create and import tables: 
    sqlite3 cars.db < database_building/create_table.sql
    sqlite3 cars.db  < database_building/import_table.sql
- Execute data_cleaning.py to get the cleaned table : first_run_2017_CleanDataset
## Modelisation and MLflow
- Execute modelisation.py
- Launch MLflow : mlflow ui
## Store your private infos in a private file
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
## Deploy the API
- Build the Docker Image: 
    - test l'image en locale:
        - docker build -t dockerimage3:latest -f api/Dockerfile .
        - docker run -p 8000:8001 dockerimage3:latest
        - then /docs
        Remark: Each time you build a new image, you have to go to Docker extension in vscode to delete the existant containers.
    - tag the image before pushing it to dockerhub
        -

    - Before pushing the image to Azure, tag the Docker Image with the Azure Container Registry (ACR) repository location. 
        Via Azure Portal:
            - Log in to the Azure portal (https://portal.azure.com).
            - Navigate to "Create a resource" > "Containers" > "Container Registry".
            - Fill in the required details like subscription, resource group, registry name, region, SKU (choose Basic, Standard, or Premium), and admin user access.
            - Click "Review + create" and then "Create" to create the registry.
        docker tag <local-image-name> <acr-login-server>/<image-name>:<tag>
        ( docker tag dockerimage registryrola.azurecr.io/dockerimage:v1 )
    - Push your Docker image to Azure Container Registry: 
        docker push <acr-login-server>/<image-name>:<tag>
        docker push registryrola.azurecr.io/dockerimage:v1
    Alternatively usint the terminal:
        - az acr create --resource-group <resource-group-name> --name <acr-name> --sku Basic --location <azure-region>

        - docker build -t dockerimage2 -f api/Dockerfile .
        - az acr login --name registryrola
        - docker tag dockerimage2:latest registryrola.azurecr.io/dockerimage2:latest
        - docker push registryrola.azurecr.io/dockerimage2:latest
    Remark: to display all available docker images : docker images -a






