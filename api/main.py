# main.py script
# This is the entry point of the FastAPI application. It initializes the FastAPI app, includes the prediction router, and sets up the database connection.
from fastapi import FastAPI, Depends
from api.database import Base
import api.predict
from api.utils import has_access
from fastapi import FastAPI
from fastapi.params import Depends
import sys
import uvicorn
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy import create_engine

# Initialize FastAPI
app = FastAPI()

# routes
PROTECTED = [Depends(has_access)]

app.include_router(
    api.predict.router,
    prefix="/predict",
    dependencies=PROTECTED
)

if __name__ == "__main__":
    DATABASE_URL = os.environ.get("DATABASE_URL")

    # Connect to the SQLite database specified in the .env file.
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    # Session Management: SessionLocal provides session management for the database.
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # Base Model: Base is the declarative base class for SQLAlchemy models.
    Base.metadata.create_all(bind=engine)
    args = sys.argv
    port = 8000 
    if len(args) > 1:
        port_string = args[1]
        port = int(port_string)

    uvicorn.run(app, host="0.0.0.0", port=port)
    
# To run this FastAPI application, you can use the uvicorn server en mode module -m:
# python3 -m api.main 


