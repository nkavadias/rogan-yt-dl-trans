# rogan-yt-dl-trans

Azure Function App written in PowerShell for YouTube download and transcription.

## Prerequisites

- [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) (v4.x or later)
- [PowerShell 7.2](https://docs.microsoft.com/powershell/scripting/install/installing-powershell) or later
- [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) (optional, for deployment)
- An Azure subscription (for deployment to Azure)

## Project Structure

```
.
├── host.json                 # Function App host configuration
├── local.settings.json       # Local development settings (not committed)
├── profile.ps1              # PowerShell profile for cold starts
├── requirements.psd1        # PowerShell module dependencies
├── .gitignore              # Git ignore file
└── HttpTrigger/            # Example HTTP trigger function
    ├── function.json       # Function binding configuration
    └── run.ps1            # Function implementation
```

## Local Development

### 1. Install Dependencies

Make sure you have Azure Functions Core Tools installed:

```bash
# For Windows (using Chocolatey)
choco install azure-functions-core-tools

# For macOS (using Homebrew)
brew tap azure/functions
brew install azure-functions-core-tools@4

# For Linux (Ubuntu/Debian)
wget -q https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update
sudo apt-get install azure-functions-core-tools-4
```

### 2. Configure Local Settings

The `local.settings.json` file contains local development settings. Update it with your configuration:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "powershell",
    "FUNCTIONS_WORKER_RUNTIME_VERSION": "7.2"
  }
}
```

### 3. Run Locally

Start the function app locally:

```bash
func start
```

The function will be available at `http://localhost:7071/api/HttpTrigger`

### 4. Test the Function

Test using curl:

```bash
# GET request with query parameter
curl "http://localhost:7071/api/HttpTrigger?name=YourName"

# POST request with JSON body
curl -X POST http://localhost:7071/api/HttpTrigger \
  -H "Content-Type: application/json" \
  -d '{"name":"YourName"}'
```

## Deployment to Azure

### Using Azure CLI

1. Login to Azure:
```bash
az login
```

2. Create a resource group:
```bash
az group create --name rogan-yt-dl-rg --location eastus
```

3. Create a storage account:
```bash
az storage account create --name roganytdlstorage --location eastus \
  --resource-group rogan-yt-dl-rg --sku Standard_LRS
```

4. Create a function app:
```bash
az functionapp create --resource-group rogan-yt-dl-rg \
  --consumption-plan-location eastus --runtime powershell \
  --runtime-version 7.2 --functions-version 4 \
  --name rogan-yt-dl-func --storage-account roganytdlstorage
```

5. Deploy the function:
```bash
func azure functionapp publish rogan-yt-dl-func
```

### Using VS Code

1. Install the [Azure Functions extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
2. Sign in to Azure
3. Click the Azure icon in the Activity Bar
4. In the Functions area, click the "Deploy to Function App" button
5. Follow the prompts to deploy

## Adding PowerShell Modules

To add PowerShell modules as dependencies, edit `requirements.psd1`:

```powershell
@{
    'Az' = '11.*'
    'PSYouTube' = '1.*'
}
```

The modules will be automatically installed by the Azure Functions runtime.

## Function Configuration

### HTTP Trigger

The `HttpTrigger` function demonstrates:
- HTTP GET and POST methods
- Query parameter handling
- Request body parsing
- HTTP response creation

Modify `HttpTrigger/run.ps1` to implement your custom logic.

## Environment Variables

Add environment variables in:
- **Local development**: `local.settings.json` under `Values`
- **Azure deployment**: Function App Configuration → Application Settings

## Logging

Use PowerShell's `Write-Host` or `Write-Information` cmdlets for logging:

```powershell
Write-Host "Processing request for: $name"
Write-Information "Additional details"
```

Logs are visible in:
- Local: Console output
- Azure: Application Insights / Log Stream

## License

See [LICENSE](LICENSE) file for details.