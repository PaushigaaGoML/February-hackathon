# February-hackathon
Building an Adaptive Multi-Agent Systems for Dynamic Task

## Folder Structure
February-hackathon/
├── hackathon/
│   ├── bin/
│   │   ├── activate
│   │   ├── activate.csh
│   │   ├── activate.fish
│   │   ├── Activate.ps1
│   │   └── ...
│   ├── etc/
│   ├── include/
│   ├── lib/
│   ├── lib64/
│   ├── pip.conf
│   ├── pyvenv.cfg
│   └── share/
├── src/
│   ├── __pycache__/
│   ├── agents/
│   │   ├── agent_chat.py
│   │   ├── agent_models.py
│   │   ├── general_practitioner_agent.py
│   │   └── specialist_agents.py
│   ├── report.py
│   ├── schema/
│   └── utils/
├── temp/
│   ├── abdomen-mri-with-contrast-sample-report-1.pdf
│   └── sterling-accuris-pathology-sample-report-unlocked-1-3.pdf
├── test/
│   ├── abdomen-mri-with-contrast-sample-report-1.pdf
│   └── sterling-accuris-pathology-sample-report-unlocked-1-3.pdf
├── .env
├── .gitignore
├── LICENSE
├── main.py
├── medical_report.pdf
├── README.md
└── requirements.txt

## Folder Contents
**src/**
This folder contains the source code for the project, including the AI agents, report generation logic, and utility functions.

**agents/**: Contains the AI agents responsible for handling different medical specializations and interactions.

**agent_chat.py**: Defines the chat functionality for interacting with the AI agents.

**agent_models.py**: Contains the models used by the AI agents.
general_practitioner_agent.py: Defines the general practitioner agent responsible for initial patient assessments.

**specialist_agents.py**: Defines the specialist agents for various medical fields.

**report.py**: Contains functions for generating medical reports in different formats (PDF, image, text).

**schema/**: Contains schema definitions for validating and structuring data.

**utils/**: Contains utility functions and helpers used throughout the project.

**temp/**
This folder is used for temporary storage of files, such as uploaded medical reports and generated reports.

**test/**
This folder contains test files and sample reports used for testing the functionality of the project.

abdomen-mri-with-contrast-sample-report-1.pdf: Sample medical report in PDF format for testing.
sterling-accuris-pathology-sample-report-unlocked-1-3.pdf: Another sample medical report in PDF format for testing.

**.env**
This file contains environment variables used by the project. It is used to configure settings such as API keys, database connections, and other sensitive information.

**.gitignore**
This file specifies which files and directories should be ignored by Git. It helps to exclude unnecessary files from being tracked in the version control system.

**LICENSE**
This file contains the license information for the project, specifying the terms under which the project's code can be used, modified, and distributed.

**main.py**
This is the main entry point for the project. It contains the code to initialize the Streamlit interface, handle user authentication, and manage the main functionalities such as report generation and chat with specialists.

**medical_report.pdf**
This file is an example of a generated medical report in PDF format.

**README.md**
This file contains the documentation for the project, including an overview, setup instructions, and technical details.

**requirements.txt**
This file lists the Python packages and dependencies required for the project. It is used to install the necessary packages using pip.

Each folder and file in the project is organized to ensure a clear separation of concerns, making the project easier to maintain and extend.


## Setup Process

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd February-hackathon
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv hackathon
    ```

3. **Activate the virtual environment:**
    - On Windows:
        ```sh
        hackathon\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source hackathon/bin/activate
        ```

4. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
5. **Install Poppler utils on windows**
https://medium.com/towards-data-science/poppler-on-windows-179af0e50150

**For Mac/Linux:**
  ```sh
  sudo apt-get install poppler-utils 
  ```

6. **Run the main script:**
    ```sh
    streamlit run main.py
    ```

7. **Login Credentials**
username: admin
password: admin

## Additional Information

- **Source Code:** The source code for the agents and utilities can be found in the src directory.
- **Reports:** Sample medical reports are located in the temp and test directories.
- **Configuration:** Environment variables can be set in the .env file.

# Technical Details

## Main Components

### Streamlit Interface  
The project uses **Streamlit** to create an interactive web interface for users to:  
- Log in  
- Generate reports  
- Chat with specialists  

### Report Generation  
The system can generate medical reports in **PDF, image, and text formats**.  
- Report generation functions are defined in `report.py`.  

### Chat with Specialists  
Users can interact with various medical specialists through a chat interface.  
- The chat functionality is managed by the `chat_with_specialist` function in `main.py`.  
- **LLM Used:** GPT-4o handles chat responses for both general practitioners and specialist agents.

## Agents  

The project uses **AutoGen** to manage multiple AI agents that provide specialized medical information.  
These agents are defined in:  
- `agent_chat.py`  
- `src/agents/general_practitioner_agent.py`  
- `specialist_agents.py`  

### List of Agents  

#### **General Practitioner (GP) Agent**  
- Conducts an initial assessment of the patient's medical data.  
- Determines the priority and order of specialist consultations.  
- **Defined in:** `src/agents/general_practitioner_agent.py`.  
- **LLM Used:** GPT-4o.  

#### **Specialist Agents**  
There are a total of 24 specialist agents, each specialist agent is responsible for providing responses related to their specific field. The agents include:  

- **Cardiologist**  
- **Oncologist**  
- **Neurologist**  
- **Endocrinologist**  
- **Pulmonologist**  
- **Nephrologist**  
- **Gastroenterologist**  
- **Hematologist**  
- **Rheumatologist**  
- **Dermatologist**  
- **Ophthalmologist**  
- **Otolaryngologist**  
- **Urologist**  
- **Gynecologist**  
- **Obstetrician**  
- **Orthopedic Surgeon**  
- **Pediatrician**  
- **Psychiatrist**  
- **Geriatrist**  
- **Infectious Disease Specialist**  
- **Allergist Immunologist**  
- **Anesthesiologist**  
- **Radiologist**  
- **Pathologist**  

These agents are defined in `agent_chat.py` and `specialist_agents.py`.  
- **LLM Used:** GPT-4o for chat responses.  

### **Why Use Agents?**  
The use of specialized agents allows the system to provide **accurate and relevant medical information** tailored to specific fields.  
- Each agent is designed to handle queries related to their specialty.  
- Ensures that users receive **expert advice and information**.  

## AI and Report Processing  

### **PDF, Image, and Text Parsing**  
- **LLM Used:** GPT-4o-mini  
- **Purpose:** Extracts patient data from **lab reports and scan reports** in PDF and image formats.  
- **Why Use It?**  
  - Handles text, tables, and image-based extraction.  
  - Optimized for document parsing and structured data extraction.  

## Functions  

| Function                     | Description                                | Defined in  |
|------------------------------|--------------------------------------------|------------|
| **Login Function**            | Manages user authentication.              | `main.py`  |
| **Main Page Function**        | Displays the main interface after login.  | `main.py`  |
| **Get Report Function**       | Handles the report generation process.    | `main.py`  |
| **Chat with Specialist**      | Manages the chat interface with specialists. | `main.py`  |

## Libraries and Tools  

### **ReportLab**  
- **Package:** `reportlab`  
- **Purpose:** Used to generate PDF reports. It provides tools to create complex documents with text, images, and graphics.  
- **Why Use It?**  
  - Powerful library for creating PDFs programmatically.  
  - Suitable for generating medical reports in various formats.  

## Utility Functions  

### **Report Generation Utilities**  
- **Files:** `report_generator.py`  
- **Purpose:** Contains utility functions to assist with report generation and other tasks.  
- **Why Use Them?**  
  - Helps modularize the code  
  - Improves maintainability and reusability  

## Summary  

| Tool/Library     | Purpose |
|-----------------|---------|
| **Streamlit**   | Used for creating the web interface due to its simplicity and real-time update capabilities. |
| **AutoGen**     | Used to manage AI agents for dynamic and specialized responses. |
| **GPT-4o**      | Used for chat responses from general practitioners and specialists. |
| **GPT-4o-mini** | Used for extracting patient data from lab reports and scan documents. |
| **ReportLab**   | Chosen for generating PDF reports because of its powerful document creation tools. |
| **JSON**        | Utilized for data interchange due to its lightweight and easy-to-parse nature. |
| **Custom AI Models** | Implemented to provide specialized medical information, ensuring accuracy and relevance. |
| **Utility Functions** | Employed to modularize the code, enhancing maintainability and reusability. |

These tools and libraries were selected to ensure the project is **efficient, maintainable, and capable of providing accurate medical information** through an interactive web interface.

Feel free to explore the project!
