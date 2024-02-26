import json
import os

# Load your JSON menu structure
menu = {
    "Salesforce Setup & Configuration": {
        "Standard Objects": [],
        "Custom Objects and Fields": [],
        "Validation Rules": [],
        "Workflows & Process Builder": [],
        "Approval Processes": [],
        "Security & Sharing (Profiles, Roles, Permission Sets)": []
    },
    "Salesforce Development": {
        "Apex (Triggers, Classes, Test Coverage)": [],
        "Visualforce": [],
        "Lightning Components (Aura & LWC)": [],
        "Integration (APIs, REST, SOAP)": []
    },
    "Platform Tools": {
        "Data Loader": [],
        "Developer Console": [],
        "Sandbox Environments": [],
        "Deployment Tools (Change Sets, ANT)": []
    },
    "Best Practices": {
        "Documentation Standards": [],
        "Code Style Guide": [],
        "Naming Conventions": [],
        "Change Management": []
    },
    "Troubleshooting": {
        "Common Errors and Solutions": [],
        "Debugging Techniques": [],
        "Performance Optimization": []
    },
    "Business Processes": {
        "Lead Generation and Qualification": {
            "Marketing Campaigns & Lead Sources": [],
            "Lead Qualification Criteria": [],
            "Lead Routing and Assignment": []
        },
        "Opportunity Management": {
            "Sales Stages and Definitions": [],
            "Forecasting and Pipeline Management": [],
            "Discounting and Approval Processes": []
        },
        "Quoting & Order Management": {
            "Product Catalog and Pricing": [],
            "Quote Generation": [],
            "Contract and Order Processing": []
        },
        "Customer Onboarding": {
            "Handoff from Sales to Implementation": [],
            "Project Kickoff and Success Criteria": []
        },
        "Customer Support & Success": {
            "Case Management Process": [],
            "Knowledge Base": [],
            "Renewal & Upsell Processes": []
        },
        "Reporting and Analytics": {
            "Key Performance Indicators (KPIs)": [],
            "Standard Reports and Dashboards": []
        },
        "Human Resources (HR) Processes": {
            "Onboarding Process": {
                "Pre-Onboarding Preparations": [],
                "First Encounters": []
            },
            "Offboarding Process": [],
            "Training and Development": [],
            "Performance Management": {
                "Performance and Development": [],
                "Continuous Improvement": []
            },
            "Conflict Resolution Framework": []
        },
        "Team Collaboration": {
            "Project Assignment Guidelines": [],
            "Project and Team Integration": [],
            "Conflict Management": []
        },
        "Company Information": {
            "Welcome to the Site": []
        }
    }
}

# Assuming your Docusaurus project has a standard '/docs' directory
docs_path = 'docs'



def create_directory_structure(menu_data, current_path):
    for key, value in menu_data.items():
        # Create a directory for the current key and prepare the filename
        folder_path = os.path.join(current_path, key).replace("&", "and").replace("(", "").replace(")", "")
        os.makedirs(folder_path, exist_ok=True)
        print("Creating folder: ", folder_path)
        filepath = os.path.join(folder_path, key + ".md").replace("&", "and").replace("(", "").replace(")", "")
        with open(filepath, "w") as f:
                f.write("# " + key)
        # Create a new path for the next level
        new_path = os.path.join(current_path, key).replace("&", "and").replace("(", "").replace(")", "")

            
        # If the value is an empty list, create an empty file
        if isinstance(value, list) and not value:
            filepath = os.path.join(new_path, key + ".md").replace("&", "and").replace("(", "").replace(")", "")
            with open(filepath, "w") as f:
                f.write("# " + key)
                # If the value is a dictionary, call the function recursively
        if isinstance(value, dict):
            create_directory_structure(value, new_path)
        elif isinstance(value, list):
            pass
            print ("No subfolders for: ", key)
            print ("Creating a file for: ", key)
        else:
            print("Invalid value type: ", value)
            return
        
create_directory_structure(menu, docs_path)
print("Directory structure created successfully!")
