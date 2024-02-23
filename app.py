import json
import os

data=[
    {
        "title": "Onboarding Checklist",
        "description": "A comprehensive checklist to ensure all necessary steps are covered for onboarding new employees.",
        "template_markdown": "# Onboarding Checklist\n\n- Welcome email sent\n- HR paperwork completed\n- Equipment and system access setup\n- First day orientation and schedule",
        "filename": "Onboarding_Checklist.md"
    },
    {
        "title": "First Two Weeks Engagement",
        "description": "A plan detailing daily and weekly goals for new employees, focusing on integration and initial training.",
        "template_markdown": "# First Two Weeks Engagement\n\n- Daily check-ins\n- Role-specific training sessions\n- Introduction to team and key projects",
        "filename": "First_Two_Weeks_Engagement.md"
    },
    {
        "title": "Technical Setup Process",
        "description": "Outlines the process for setting up access to technical systems and tools, including Salesforce.",
        "template_markdown": "# Technical Setup Process\n\n- Salesforce access configuration\n- Email and communication tools setup\n- Hardware and software requirements",
        "filename": "Technical_Setup_Process.md"
    },
    {
        "title": "Training and Development Plan",
        "description": "A structured plan covering essential skills, Salesforce competencies, and professional development.",
        "template_markdown": "# Training and Development Plan\n\n- Salesforce fundamentals\n- Company policies and culture\n- Ongoing learning opportunities",
        "filename": "Training_and_Development_Plan.md"
    },
    {
        "title": "Performance Evaluation Criteria",
        "description": "Defines the criteria and process for evaluating the performance of new employees.",
        "template_markdown": "# Performance Evaluation Criteria\n\n- Specific goals and objectives\n- Feedback mechanisms\n- Regular review sessions",
        "filename": "Performance_Evaluation_Criteria.md"
    },
    {
        "title": "Regular Check-in Schedule",
        "description": "Establishes a schedule for regular meetings between managers and new employees to discuss progress and concerns.",
        "template_markdown": "# Regular Check-in Schedule\n\n- Weekly one-on-one meetings\n- Goals and expectations review\n- Support and feedback",
        "filename": "Regular_Check-in_Schedule.md"
    },
    {
        "title": "Project Assignment Guidelines",
        "description": "Provides guidelines for assigning new employees to projects, including scope and expectations.",
        "template_markdown": "# Project Assignment Guidelines\n\n- Project selection criteria\n- Expectations and deliverables\n- Support and resources available",
        "filename": "Project_Assignment_Guidelines.md"
    },
    {
        "title": "Feedback and Continuous Improvement Process",
        "description": "Details the process for giving and receiving feedback, and for fostering continuous improvement.",
        "template_markdown": "# Feedback and Continuous Improvement Process\n\n- Regular feedback sessions\n- Mechanisms for suggestions\n- Implementation of improvements",
        "filename": "Feedback_and_Continuous_Improvement_Process.md"
    },
    {
        "title": "Conflict Resolution Framework",
        "description": "Outlines steps for resolving conflicts within the team, promoting a positive work environment.",
        "template_markdown": "# Conflict Resolution Framework\n\n- Steps for addressing conflicts\n- Communication guidelines\n- Escalation paths",
        "filename": "Conflict_Resolution_Framework.md"
    },
    {
        "title": "Offboarding Process",
        "description": "Describes the process for offboarding employees, ensuring a smooth transition and knowledge transfer.",
        "template_markdown": "# Offboarding Process\n\n- Knowledge transfer steps\n- System access revocation\n- Exit interviews and feedback",
        "filename": "Offboarding_Process.md"
    }]
code = """
    # Re-create the folder structure and prepare markdown files for the wiki format, following the previous plan

    import os

    # Define the base path for the folder structure
    base_path = "/mnt/data/salesforce_onboarding"

    # Function to set up the folder structure and markdown files
    def setup_folders_and_files():
    # Define the folders and files structure
    folders_files = {
    "Onboarding_Checklist": "Onboarding_Checklist.md",
    "First_Two_Weeks_Engagement": "First_Two_Weeks_Engagement.md",
    "Technical_Setup_Process": "Technical_Setup_Process.md",
    "Training_and_Development_Plan": "Training_and_Development_Plan.md",
    # Placeholder for additional templates
    }

    # Create base folder if it doesn't exist
    if not os.path.exists(base_path):
    os.makedirs(base_path)

    # Create folders and files
    for folder, file in folders_files.items():
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, file)
    with open(file_path,
    "w") as f:
            f.write(f"# {folder.replace('_', ' ')}\n\n> Placeholder content for {folder.replace('_', ' ')}.")

            # Execute the function to set up the folder structure and markdown files
            setup_folders_and_files()

            # Confirm the creation
            "Folder structure and initial markdown files created successfully."

            # Next steps will involve packaging this structure into a downloadable format for local extraction and memory.

        """
tree="""    
    Salesforce_Onboarding/
    ├── Onboarding_Checklist/
    │   └── Onboarding_Checklist.md
    ├── First_Two_Weeks_Engagement/
    │   └── First_Two_Weeks_Engagement.md
    ├── Technical_Setup_Process/
    │   └── Technical_Setup_Process.md
    ├── Training_and_Development_Plan/
    │   └── Training_and_Development_Plan.md
    ├── Performance_Evaluation_Criteria/
    │   └── Performance_Evaluation_Criteria.md
    ├── Regular_Check-in_Schedule/
    │   └── Regular_Check-in_Schedule.md
    ├── Project_Assignment_Guidelines/
    │   └── Project_Assignment_Guidelines.md
    ├── Feedback_and_Continuous_Improvement_Process/
    │   └── Feedback_and_Continuous_Improvement_Process.md
    ├── Conflict_Resolution_Framework/
    │   └── Conflict_Resolution_Framework.md
    └── Offboarding_Process/
        └── Offboarding_Process.md
    """


def python_notebook_create_ipynb_json_with_data_and_code(filename,data,code,tree):
    import json
    # Create a dictionary with the notebook components
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Salesforce Onboarding Process\n",
                    "This notebook simulates the process of creating a folder structure and markdown files for the Salesforce onboarding process."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Folder Structure and Markdown Files\n",
                    "The first step is to create the folder structure and markdown files for the onboarding process."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": 1,
                "metadata": {},
                "outputs": [],
                "source": [
                    code
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Folder Structure\n",
                    "The folder structure has been created as follows:\n",
                    "```\n",
                    tree,
                    "```"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 3. Conclusion\n",
                    "The folder structure and initial markdown files have been created successfully."
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    # Convert the notebook to a JSON-formatted string
    notebook_json = json.dumps(notebook, indent=2)

    # Save the notebook JSON string to a file
    with open(filename, "w") as file:
        file.write(notebook_json)
    return notebook_json

def python_notebook_create_ipynb_raw_json(filename,notebook_json):
    import json
    # Load the notebook JSON string from the file
    with open(filename
    ) as file:
        notebook_json = file.read()

    # Convert the notebook JSON string to a dictionary
    notebook = json.loads(notebook_json)

    # Print the notebook dictionary
    print(notebook)

    # Convert the notebook dictionary to a JSON-formatted string
    notebook_json = json.dumps(notebook, indent=2)

    # Print the notebook JSON string
    print(notebook_json)
    return notebook_json

def python_notebook_create_ipynb_json_with_data(filename,data):
    import json
    # Create a dictionary with the notebook components
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Salesforce Onboarding Process\n",
                    "This notebook simulates the process of creating a folder structure and markdown files for the Salesforce onboarding process."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Folder Structure and Markdown Files\n",
                    "The first step is to create the folder structure and markdown files for the onboarding process."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    data
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Folder Structure\n",
                    "The folder structure has been created as follows:\n",
                    "```\n",
                    tree,
                    "```"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 3. Conclusion\n",
                    "The folder structure and initial markdown files have been created successfully."
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.8"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    # Convert the notebook to a JSON-formatted string
    notebook_json = json.dumps(notebook, indent=2)

    # Save the notebook JSON string to a file
    with open(filename, "w") as file:
        file.write(notebook_json)
    return notebook_json

def python_notebook_create_ipynb_json(filename):
    import json
    # Create a dictionary with the notebook components
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Salesforce Onboarding Process\n",
                    "This notebook simulates the process of creating a folder structure and markdown files for the Salesforce onboarding process."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Folder Structure and Markdown Files\n",
                    "The first step is to create the folder structure and markdown files for the onboarding process."
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "### Onboarding Checklist\n",
                    "A comprehensive checklist to ensure all necessary steps are covered for onboarding new employees.\n",
                    "- **Filename**: Onboarding_Checklist.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Onboarding_Checklist/Onboarding_Checklist.md\n",
                    "---\n",
                    "### First Two Weeks Engagement\n",
                    "A plan detailing daily and weekly goals for new employees, focusing on integration and initial training.\n",
                    "- **Filename**: First_Two_Weeks_Engagement.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/First_Two_Weeks_Engagement/First_Two_Weeks_Engagement.md\n",
                    "---\n",
                    "### Technical Setup Process\n",
                    "Outlines the process for setting up access to technical systems and tools, including Salesforce.\n",
                    "- **Filename**: Technical_Setup_Process.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Technical_Setup_Process/Technical_Setup_Process.md\n",
                    "---\n",
                    "### Training and Development Plan\n",
                    "A structured plan covering essential skills, Salesforce competencies, and professional development.\n",
                    "- **Filename**: Training_and_Development_Plan.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Training_and_Development_Plan/Training_and_Development_Plan.md\n",
                    "---\n",
                    "### Performance Evaluation Criteria\n",
                    "Defines the criteria and process for evaluating the performance of new employees.\n",
                    "- **Filename**: Performance_Evaluation_Criteria.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Performance_Evaluation_Criteria/Performance_Evaluation_Criteria.md\n",
                    "---\n",
                    "### Regular Check-in Schedule\n",
                    "Establishes a schedule for regular meetings between managers and new employees to discuss progress and concerns.\n",
                    "- **Filename**: Regular_Check-in_Schedule.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Regular_Check-in_Schedule/Regular_Check-in_Schedule.md\n",
                    "---\n",
                    "### Project Assignment Guidelines\n",
                    "Provides guidelines for assigning new employees to projects, including scope and expectations.\n",
                    "- **Filename**: Project_Assignment_Guidelines.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Project_Assignment_G uidelines/Project_Assignment_Guidelines.md\n",
                    "---\n",
                    "### Feedback and Continuous Improvement Process\n",
                    "Details the process for giving and receiving feedback, and for fostering continuous improvement.\n",
                    "- **Filename**: Feedback_and_Continuous_Improvement_Process.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Feedback_and_Continuous_Improvement_Process/Feedback_and_Continuous_Improvement_Process.md\n",
                    "---\n",
                    "### Conflict Resolution Framework\n",
                    "Outlines steps for resolving conflicts within the team, promoting a positive work environment.\n",
                    "- **Filename**: Conflict_Resolution_Framework.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Conflict_Resolution_Framework/Conflict_Resolution_Framework.md\n",
                    "---\n",
                    "### Offboarding Process\n",
                    "Describes the process for offboarding employees, ensuring a smooth transition and knowledge transfer.\n",
                    "- **Filename**: Offboarding_Process.md\n",
                    "- **Path**: /mnt/data/salesforce_onboarding/Offboarding_Process/Offboarding_Process.md"
                ]
            },

            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Folder Structure\n",
                    "The folder structure has been created as follows:\n",
                    "```\n",
                    tree,
                    "```"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 3. Conclusion\n",
                    "The folder structure and initial markdown files have been created successfully."
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.8"
            }
        },

        "nbformat": 4,
        "nbformat_minor": 4
    }
    # Convert the notebook to a JSON-formatted string
    notebook_json = json.dumps(notebook, indent=2)

    # Save the notebook JSON string to a file
    with open(filename, "w") as file:
        file.write(notebook_json)
    return notebook_json

    

def create_folder_and_template_markdown(data, base_path = "/mnt/data/salesforce_onboarding"):
    # Function to set up the folder structure and markdown files
    def setup_folders_and_files():
        # Create base folder if it doesn't exist
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        # Create folders and files
        for template in data:
            folder_path = os.path.join(base_path, template["title"].replace(" ", "_"))
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, template["filename"])
            with open(file_path, "w") as f:
                f.write(template["template_markdown"])

    # Execute the function to set up the folder structure and markdown files
    setup_folders_and_files()

    # Confirm the creation
    return "Folder structure and initial markdown files created successfully."

def create_prompts_for_markdown(data):
    # Create prompts for the markdown files
    prompts = []
    for template in data:
        prompt = f"### {template['title']}\n\n{template['description']}\n\n- **Filename**: {template['filename']}\n\n- **Path**: /mnt/data/salesforce_onboarding/{template['title'].replace(' ', '_')}/{template['filename']}\n\n---"
        prompts.append(prompt)

    # Combine the prompts into a single string, separated by newlines
    prompts_str = "\n".join(prompts)

    # Return the prompts string
    return prompts_str

def main():
    # Create the folder structure and markdown files
    result = create_folder_and_template_markdown(data, '.')

    # Print the result
    print(result)

    # Create prompts for the markdown files
    prompts = create_prompts_for_markdown(data)

    # Print the prompts
    print(prompts)
    
    # Create a notebook with the data and code
    notebook_json = python_notebook_create_ipynb_json_with_data_and_code("Salesforce_Onboarding_Process_Simulation.ipynb",data,code,tree)
    print(notebook_json)
    
    notebook_json = python_notebook_create_ipynb_raw_json("Salesforce_Onboarding_Process_Simulation.ipynb",notebook_json)
    print(notebook_json)
        
main()

        