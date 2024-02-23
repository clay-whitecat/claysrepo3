#!/bin/bash

# Check Bash version compatibility
if ((BASH_VERSINFO[0] < 4)); then
    echo "This script requires Bash version 4.0 or higher. You are using ${BASH_VERSION}."
    exit 1
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Create and activate a Python virtual environment
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    python3.11 -m venv "$VENV_DIR"
fi
source "$VENV_DIR/bin/activate"

# Upgrade pip to the latest version
pip install --upgrade pip

# Declare an associative array for wikis and their installation methods
declare -A wikis=(
    [mkdocs]="pip"
    [docusaurus]="npm"
    [vuepress]="npm"
    [gatsby-cli]="npm"
    [hugo]="brew"
)

# Iterate through wikis and install if not found
for wiki in "${!wikis[@]}"; do
    echo "Checking for $wiki..."
    if command_exists $wiki; then
        echo "$wiki is installed."
    else
        echo "$wiki could not be found. Attempting to install..."
        case ${wikis[$wiki]} in
            pip)
                pip install $wiki
                ;;
            npm)
                if [ "$wiki" == "docusaurus" ]; then
                    npx @docusaurus/init@latest init my-website classic
                else
                    npm install -g $wiki
                fi
                ;;
            brew)
                brew install $wiki || echo "No brew package found for $wiki. Please install manually."
                ;;
            *)
                echo "Unknown installation method for $wiki."
                ;;
        esac
    fi
done

# Deactivate the Python virtual environment
deactivate

echo "Script execution completed."

# if folders is docs/ then rename folders so that _ is replaced 
# with a space and then run the script

for f in docs/*; do
    mv -- "$f" "${f//_/ }"
done

# cli one liner to run the script on docs folder and rename them
# find docs/ -type d -exec bash -c 'mv -- "$1" "${1//_/ }"' _ {} \;
