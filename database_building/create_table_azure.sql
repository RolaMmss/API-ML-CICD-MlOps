-- create_table_azure.sql

CREATE TABLE CarPredictions (
    id INT PRIMARY KEY IDENTITY(1,1),
    etat_de_route NVARCHAR(50),
    carburant NVARCHAR(50),
    turbo NVARCHAR(50),
    nombre_portes NVARCHAR(50),
    type_vehicule NVARCHAR(50),
    roues_motrices NVARCHAR(50),
    emplacement_moteur NVARCHAR(50),
    empattement FLOAT,
    longueur FLOAT,
    largeur FLOAT,
    hauteur FLOAT,
    poids_vehicule FLOAT,
    type_moteur NVARCHAR(50),
    nombre_cylindres NVARCHAR(50),
    taille_moteur FLOAT,
    systeme_carburant NVARCHAR(50),
    taux_alésage FLOAT,
    course FLOAT,
    taux_compression FLOAT,
    chevaux INT,
    tour_moteur INT,
    consommation_ville FLOAT,
    consommation_autoroute FLOAT,
    marque NVARCHAR(50),
    modèle NVARCHAR(50),
    predicted_price FLOAT,
    prediction_time DATETIME DEFAULT GETDATE()
);










