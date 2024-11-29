#!/bin/bash

# Create new directory structure
mkdir -p new_structure/{automation,tools,web,media,learning,security,utils}

# Automation related projects
mv confluence_automation google_automation mbox_automation DesktopAutomation new_structure/automation/
mv podman elementCopy new_structure/automation/

# Development tools and utilities
mv RegexGenerator codeSearch remove_duplicate_files new_structure/tools/
mv .vscode new_structure/tools/ide_config

# Web related projects
mv Ductube moderateFacebookGroup.js Facebook_Messages_Report.py new_structure/web/

# Media handling
mv images media.py simple_image_hash.py ebook_to_audiobook.py new_structure/media/
mv Blender motion_amplification new_structure/media/

# Learning and documentation
mv learning Career ShellCommands.md links.md new_structure/learning/
mv README.md new_structure/

# Security related
mv dangerous_places sendSecrets new_structure/security/

# Miscellaneous utilities
mv app_ideas domains links semanticSearchAllTheThings new_structure/utils/
mv bacteriasim.html merge_dir_for_GPT.ps1 output_file.txt new_structure/utils/

# Move .gitignore to root
mv .gitignore new_structure/

# Create a new README.md in the root directory
cat > new_structure/README.md << 'EOF'
# Repository Structure

This repository contains various automation tools and utilities organized as follows:

## /automation
- Confluence automation scripts
- Google workspace automation
- Desktop automation tools
- Container and deployment automation

## /tools
- Regex generation utilities
- Code search tools
- Duplicate file removal tools
- IDE configurations

## /web
- Web applications and scripts
- Social media automation tools

## /media
- Image processing utilities
- Audio/video conversion tools
- 3D modeling and animation

## /learning
- Documentation and guides
- Career resources
- Learning materials

## /security
- Security-related tools
- Encryption utilities

## /utils
- Miscellaneous utilities
- Domain management
- Application ideas and prototypes
EOF

# Backup original structure
echo "Creating backup of original structure..."
mkdir -p backup_$(date +%Y%m%d)
cp -r $(ls -A | grep -v "new_structure\|backup_") backup_$(date +%Y%m%d)/

# Move new structure to replace old
echo "Moving new structure into place..."
mv new_structure/* .
rmdir new_structure

echo "Repository has been reorganized. Original structure backed up to backup_$(date +%Y%m%d)/"
echo "Please review changes and commit if satisfied."