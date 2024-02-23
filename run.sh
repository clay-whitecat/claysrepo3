#!/bin/bash

# Define the list of static site generators
GENERATORS=("mkdocs" "docusaurus" "vuepress" "gatsby-cli" "hugo")

# ensure the programs in the list are installed and install with brew if not
for generator in "${GENERATORS[@]}"
do
    if ! command -v $generator &> /dev/null
    then
        echo "$generator could not be found"
        echo "Installing $generator"
        # check if brew package exists for the generator by name
        if brew list --formula | grep -q $generator; then
            brew install $generator
        else
            echo "No brew package found for $generator"
            # check if pip package exists for the generator by name
            if pip list | grep -q $generator; then
                pip install $generator > /dev/null
            else
                echo "No pip package found for $generator"
                echo "Please install $generator manually"

            fi
        fi
    else
        echo "$generator is installed"
    fi  
done


# prep wikis folder and move into it supress errors if it already exists
mkdir wikis 2>/dev/null
cd wikis

for generator in "${GENERATORS[@]}"
do
    mkdir $generator
    cd $generator

    case $generator in
        "mkdocs")
            mkdocs new .
            # build
            mkdocs build
            ;;  
        "docusaurus")
            npx @docusaurus
            ;;  
        "vuepress")
            npx create-vuepress-site .
            ;;  
        "gatsby")
            gatsby new .
            ;;  
        "hugo") 
            hugo new site .
            ;;  
        *)  
            echo "Unknown generator"
            ;;      
    esac

    # Move back to the root folder
    cd ../..

done
 
  