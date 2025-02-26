# February-hackathon
Building a multi agent system

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

5. **Run the main script:**
    ```sh
    python main.py
    ```

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

## Agents  

The project uses multiple AI agents to provide specialized medical information.  
These agents are defined in:  
- `agent_chat.py`  
- `src/agents/general_practitioner_agent.py`  
- `specialist_agents.py`  

### List of Agents  

#### **General Practitioner (GP) Agent**  
- Conducts an initial assessment of the patient's medical data.  
- Determines the priority and order of specialist consultations.  
- **Defined in:** `src/agents/general_practitioner_agent.py`.  

#### **Specialist Agents**  
Each specialist agent is responsible for providing responses related to their specific field. The agents include:  

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

### **Why Use Agents?**  
The use of specialized agents allows the system to provide **accurate and relevant medical information** tailored to specific fields.  
- Each agent is designed to handle queries related to their specialty.  
- Ensures that users receive **expert advice and information**.  

## Functions  

| Function                     | Description                                | Defined in  |
|------------------------------|--------------------------------------------|------------|
| **Login Function**            | Manages user authentication.              | `main.py`  |
| **Main Page Function**        | Displays the main interface after login.  | `main.py`  |
| **Get Report Function**       | Handles the report generation process.    | `main.py`  |
| **Chat with Specialist**      | Manages the chat interface with specialists. | `main.py`  |

## Additional Information  

- **Source Code:** The source code for the agents and utilities can be found in the `src` directory.  
- **Reports:** Sample medical reports are located in the `temp` and `test` directories.  
- **Configuration:** Environment variables can be set in the `.env` file.  

---

Feel free to explore the project!
