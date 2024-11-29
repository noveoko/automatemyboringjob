# PowerShell script to remove unused files
$rootDir = "C:\Users\mrkra\OneDrive\Dokumenty\automatemyboringjob\web\Ductube"

# List of files and directories to remove
$toRemove = @(
    # Unused or duplicate files
    "src\contentScript.ts",  # duplicate of src/content/contentScript.ts
    "src\script.js",        # old implementation
    "src\index.html",       # not needed in new implementation
    "src\GoogleSearch",     # old implementation directory
    "src\redux",           # not used in new implementation
    "reorganize.ps1",      # likely a one-time script
    
    # Duplicate assets
    "assets\img\duct_tape_icon.png",  # using icon.png instead
    "src\GoogleSearch\icon.png"       # duplicate icon
)

# Function to safely remove items
function Remove-SafelyWithConfirmation {
    param (
        [string]$path
    )
    
    if (Test-Path $path) {
        $fullPath = Join-Path $rootDir $path
        $isDirectory = (Get-Item $fullPath) -is [System.IO.DirectoryInfo]
        
        Write-Host "About to remove: $path"
        $confirm = Read-Host "Are you sure you want to remove this? (y/n)"
        
        if ($confirm -eq 'y') {
            if ($isDirectory) {
                Remove-Item $fullPath -Recurse -Force
                Write-Host "Removed directory: $path"
            } else {
                Remove-Item $fullPath -Force
                Write-Host "Removed file: $path"
            }
        } else {
            Write-Host "Skipped: $path"
        }
    } else {
        Write-Host "Not found: $path"
    }
}

# Main execution
Write-Host "Starting cleanup process..."
Write-Host "Working directory: $rootDir"
Write-Host ""

foreach ($item in $toRemove) {
    Remove-SafelyWithConfirmation $item
}

Write-Host ""
Write-Host "Cleanup process completed."