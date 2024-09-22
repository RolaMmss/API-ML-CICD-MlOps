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

### Conversions:

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