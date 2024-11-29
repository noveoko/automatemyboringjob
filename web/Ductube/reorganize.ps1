# Define the base directory
$baseDir = "C:\Users\mrkra\OneDrive\Dokumenty\automatemyboringjob\web\Ductube"

# Create new directories for organization
$foldersToCreate = @("assets\img", "src\redux", "src\GoogleSearch", "docs")
foreach ($folder in $foldersToCreate) {
    $newPath = Join-Path $baseDir $folder
    if (-not (Test-Path $newPath)) {
        New-Item -ItemType Directory -Path $newPath
    }
}

# Move files to their appropriate directories
Move-Item "$baseDir\static\img\duct_tape_icon.png" "$baseDir\assets\img\" -Force
Move-Item "$baseDir\icon.png" "$baseDir\assets\" -Force
Move-Item "$baseDir\GoogleSearch\*" "$baseDir\src\GoogleSearch\" -Force
Move-Item "$baseDir\redux\*" "$baseDir\src\redux\" -Force
Move-Item "$baseDir\script.js" "$baseDir\src\" -Force
Move-Item "$baseDir\manifest.json" "$baseDir\src\" -Force
Move-Item "$baseDir\index.html" "$baseDir\src\" -Force
Move-Item "$baseDir\README.md" "$baseDir\docs\" -Force
Move-Item "$baseDir\credit.html" "$baseDir\docs\" -Force

# Remove empty directories
$directoriesToRemove = @("static", "GoogleSearch", "redux")
foreach ($dir in $directoriesToRemove) {
    $dirPath = Join-Path $baseDir $dir
    if (Test-Path $dirPath) {
        Remove-Item -Path $dirPath -Recurse -Force
    }
}

Write-Output "Repository has been reorganized!"
