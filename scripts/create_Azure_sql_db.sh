# Step 1: Log in to Azure
az login

# Step 2: Set the Azure Subscription (if you have multiple subscriptions)
az account set --subscription "your-subscription-id"

# Step 3: Define variables for resource group, server, and database
RESOURCE_GROUP="myResourceGroup"
LOCATION="eastus"
SERVER_NAME="my-sql-server"
DB_NAME="mydatabase"
ADMIN_USER="myadmin"
PASSWORD="yourStrong!Password"

# Step 4: Create a resource group
# az group create --name $RESOURCE_GROUP --location $LOCATION

# Step 5: Create a SQL Server
az sql server create \
    --name $SERVER_NAME \
    --resource-group $RESOURCE_GROUP \
    --location $LOCATION \
    --admin-user $ADMIN_USER \
    --admin-password $PASSWORD

# Step 6: Create a SQL Database
az sql db create \
    --resource-group $RESOURCE_GROUP \
    --server $SERVER_NAME \
    --name $DB_NAME \
    --service-objective S0

# Step 7: Configure a firewall rule to allow your IP address to access the server
MY_IP=$(curl ifconfig.me)
az sql server firewall-rule create \
    --resource-group $RESOURCE_GROUP \
    --server $SERVER_NAME \
    --name AllowYourIP \
    --start-ip-address $MY_IP \
    --end-ip-address $MY_IP

# Step 8: Optionally, you can also allow Azure services to access the server
az sql server firewall-rule create \
    --resource-group $RESOURCE_GROUP \
    --server $SERVER_NAME \
    --name AllowAzureServices \
    --start-ip-address 0.0.0.0 \
    --end-ip-address 0.0.0.0
