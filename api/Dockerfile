FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

RUN mkdir /app/api


# Install Python dependencies
COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade  -r requirements.txt

COPY . /app/api

# ENV PATH ${APP_ROOT}/.local/bin:${PATH}

# Expose the port that FastAPI runs on
EXPOSE 8000 

# Command to run the application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]