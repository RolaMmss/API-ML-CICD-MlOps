set -o allexport
# Load environment variables from .env file
source .env   
set +o allexport

# Step 1: Log in to Azure
az login

# # Step 2: Set the Azure Subscription (if you have multiple subscriptions)
# az account set --subscription "SUBSCRIPTION_ID

# # Step 3: Define variables for resource group, server, and database
# RESOURCE_GROUP="myResourceGroup"
# LOCATION="eastus"
# SERVER_NAME="my-sql-server"
# DB_NAME="mydatabase"
# ADMIN_USER="myadmin"
# PASSWORD="yourStrong!Password"

# # Step 4: Create a resource group
# # az group create --name $RESOURCE_GROUP --location $LOCATION

# # Step 5: Create a SQL Server
# az sql server create \
#     --name $SQL_SERVER_NAME \
#     --resource-group $RESOURCE_GROUP \
#     --location $LOCATION \
#     --admin-user $ADMIN_USER \
#     --admin-password $ADMIN_PASSWORD

# # Step 6: Create a SQL Database under the server
# az sql db create \
#     --resource-group $RESOURCE_GROUP \
#     --server $SQL_SERVER_NAME \
#     --name $SQL_DB_NAME \
#     --service-objective S0

# # Step 7: Configure a firewall rule to allow your IP address to access the server
# MY_IP=$(curl ifconfig.me)
# az sql server firewall-rule create \   # This command allows access from all IPs (0.0.0.0)
#     --resource-group $RESOURCE_GROUP \
#     --server $SQL_SERVER_NAME \
#     --name AllowYourIP \
#     --start-ip-address $MY_IP \
#     --end-ip-address $MY_IP

# # Step 8: Optionally, you can also allow Azure services to access the server
# az sql server firewall-rule create \
#     --resource-group $RESOURCE_GROUP \
#     --server $SERVER_NAME \
#     --name AllowAzureServices \
#     --start-ip-address 0.0.0.0 \
#     --end-ip-address 0.0.0.0


# Create SQL Server
echo "Creating Azure SQL Server: $SQL_SERVER_NAME..."
az sql server create --name $SQL_SERVER_NAME \
    --resource-group $RESSOURCE_GROUP \
    --location $LOCATION \
    --admin-user $ADMIN_USER \
    --admin-password $ADMIN_PASSWORD

# Check if the server creation succeeded
if [ $? -ne 0 ]; then
    echo "SQL Server creation failed. Please check the resource group and server parameters."
    exit 1
fi

# Create SQL Database
echo "Creating Azure SQL Database: $SQL_DB_NAME..."
az sql db create --resource-group $RESSOURCE_GROUP \
    --server $SQL_SERVER_NAME \
    --name $SQL_DB_NAME \
    --service-objective S0

# Check if the database creation succeeded
if [ $? -ne 0 ]; then
    echo "SQL Database creation failed. Please check the database parameters."
    exit 1
fi

# Configure firewall rule to allow access from all IPs
echo "Configuring firewall rule to allow access from all IPs..."
az sql server firewall-rule create --resource-group $RESSOURCE_GROUP \
    --server $SQL_SERVER_NAME \
    --name AllowAllIPs \
    --start-ip-address 0.0.0.0 \
    --end-ip-address 0.0.0.0

if [ $? -eq 0 ]; then
    echo "Azure SQL Server and Database created successfully!"
else
    echo "Failed to configure firewall rule."
fi



# Make it executable by running:     
#  chmod +x scripts/create_sql_db.sh
# Run the script:                   
#  ./scripts/create_sql_db.sh


