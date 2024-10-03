-- Execute this command to create the tables
-- sqlite3 cars.db < database_building/create_table.sql


-- Create a table named Cars with columns corresponding to the columns in your CSV file.

CREATE TABLE IF NOT EXISTS Cars (
    car_ID INTEGER PRIMARY KEY,
    symboling INTEGER,
    CarName TEXT,
    fueltype TEXT,
    aspiration TEXT,
    doornumber TEXT,
    carbody TEXT,
    drivewheel TEXT,
    enginelocation TEXT,
    wheelbase REAL,    --REAL values are stored as 8-byte floating-point numbers.
    carlength REAL,
    carwidth REAL,
    carheight REAL,
    curbweight INTEGER,
    enginetype TEXT,
    cylindernumber TEXT,
    enginesize INTEGER,
    fuelsystem TEXT,
    boreratio REAL,
    stroke REAL,
    compressionratio REAL,
    horsepower INTEGER,
    peakrpm INTEGER,
    citympg INTEGER,
    highwaympg INTEGER,
    price INTEGER
);





-- IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[Cars]') AND type in (N'U'))
-- BEGIN
--     CREATE TABLE [dbo].[Cars] (
--         car_ID INT PRIMARY KEY,
--         symboling INT,
--         CarName NVARCHAR(255),
--         fueltype NVARCHAR(50),
--         aspiration NVARCHAR(50),
--         doornumber NVARCHAR(10),
--         carbody NVARCHAR(50),
--         drivewheel NVARCHAR(50),
--         enginelocation NVARCHAR(50),
--         wheelbase FLOAT,
--         carlength FLOAT,
--         carwidth FLOAT,
--         carheight FLOAT,
--         curbweight INT,
--         enginetype NVARCHAR(50),
--         cylindernumber NVARCHAR(50),
--         enginesize INT,
--         fuelsystem NVARCHAR(50),
--         boreratio FLOAT,
--         stroke FLOAT,
--         compressionratio FLOAT,
--         horsepower INT,
--         peakrpm INT,
--         citympg INT,
--         highwaympg INT,
--         price INT
--     );
-- END
