#!/bin/bash

# Specify the technologies for .gitignore
TECHNOLOGIES="python,vscode"

# Update .gitignore
echo "Checking for .gitignore..."
if [ ! -f .gitignore ]; then
    echo ".gitignore not found. Creating a new one..."
else
    echo ".gitignore found. Updating..."
fi
curl -s -o .gitignore https://www.toptal.com/developers/gitignore/api/$TECHNOLOGIES
if [ $? -eq 0 ]; then
    echo ".gitignore updated successfully!"
else
    echo "Failed to update .gitignore. Please check your internet connection."
    exit 1
fi

# Update requirements.txt
echo "Checking for requirements.txt..."
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Creating a new one..."
    touch requirements.txt
else
    echo "requirements.txt found. Updating..."
fi

if command -v pip &> /dev/null; then
    pip freeze > temp_requirements.txt
    cat temp_requirements.txt > requirements.txt
    rm temp_requirements.txt
    echo "requirements.txt updated successfully!"
else
    echo "pip is not installed. Please install pip and try again."
    exit 1
fi

# Sort and deduplicate requirements.txt
echo "Sorting and deduplicating requirements.txt..."
sort -u requirements.txt -o requirements.txt
if [ $? -eq 0 ]; then
    echo "requirements.txt sorted and deduplicated successfully!"
else
    echo "Failed to sort requirements.txt. Please check file permissions."
    exit 1
fi

echo "All files updated successfully in the project root!"
