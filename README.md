# February-hackathon
Building a multi agent system

## Folder Structure
February-hackathon/ ├── hackathon/ │ ├── bin/ │ │ ├── activate │ │ ├── activate.csh │ │ ├── activate.fish │ │ ├── Activate.ps1 │ │ └── ... │ ├── etc/ │ ├── include/ │ ├── lib/ │ ├── lib64/ │ ├── pip.conf │ ├── pyvenv.cfg │ └── share/ ├── src/ │ ├── pycache/ │ ├── agents/ │ ├── report.py │ ├── schema/ │ └── utils/ ├── temp/ │ ├── abdomen-mri-with-contrast-sample-report-1.pdf │ └── sterling-accuris-pathology-sample-report-unlocked-1-3.pdf ├── test/ │ ├── abdomen-mri-with-contrast-sample-report-1.pdf │ └── sterling-accuris-pathology-sample-report-unlocked-1-3.pdf ├── .env ├── .gitignore ├── LICENSE ├── main.py ├── medical_report.pdf ├── README.md └── requirements.txt


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

Feel free to explore the project and contribute!