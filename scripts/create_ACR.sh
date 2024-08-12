set -o allexport
# Load environment variables from .env file
source .env   
set +o allexport

# Login to Azure
az login

az container create \
            --resource-group $RESSOURCE_GROUP \
            --name ContainerInstanceApi --image $DOCKERHUB_USERNAME/repo_docker:latest --cpu 1 \
            --memory 1 \
            --ip-address public \
            --ports 80 8000 \
            --environment-variables \
              "SUBSCRIPTION_ID"=$SUBSCRIPTION_ID \
              "RESSOURCE_GROUP"=$RESSOURCE_GROUP \
              "WORKSPACE_NAME"=$WORKSPACE_NAME \
              "SERVER"=$SERVER \
              "DATABASE"=$DATABASE \
              "POSTGRES_USER"=$POSTGRES_USER \
              "PASSWORD"=$PASSWORD \
              "SECRET_KEY"=$SECRET_KEY

# az container create \
#             --resource-group RG_Rola_certif2024 \
#             --name ContainerInstanceApi \    
#             --image rola123/repo_docker:latest \    
#             --cpu 1 \
#             --memory 1 \
#             --ip-address public \
#             --ports 80 8000 \
#              --registry-username rola123 \
#             --registry-password Do-302868