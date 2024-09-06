set -o allexport
# Load environment variables from .env file
source .env   
set +o allexport

# Login to Azure
az login

az container create \
    --resource-group $RESSOURCE_GROUP \
    --name containerinstanceapi \
    --image $DOCKERHUB_USERNAME/repo_docker:latest \
    --cpu 1 \
    --memory 1 \
    --ip-address public \
    --ports 8000 8501 \
    --registry-username $DOCKERHUB_USERNAME \
    --registry-password $DOCKERHUB_PASSWORD
