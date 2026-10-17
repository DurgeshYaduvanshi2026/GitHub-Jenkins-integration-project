# GitHub & Jenkins CI/CD Automation Project

This repository contains a Python-based test automation framework configured with **Pytest** and **Playwright**, following the industry-standard **Page Object Model (POM)** design pattern. It is fully prepared for continuous integration and continuous deployment (CI/CD) pipelines using **Jenkins**.

---

## 📁 Project Architecture & Folder Structure

The project structure follows a clean separation of concerns for scalable test automation:

```text
Github_jenkins_project/
├── .github/          # GitHub-specific workflows (Actions YAML configurations)
├── .venv/            # Isolated local Python virtual environment
├── pages/            # Page Object Model locators and interaction methods
├── reports/          # Execution outputs (HTML reports, screenshots, Allure logs)
├── testdata/         # External data sources (JSON, CSV, environment variables)
├── tests/            # Test script files following the 'test_*.py' naming convention
├── utilities/        # Reusable helper scripts, loggers, and database connectors
├── config.py         # Global configuration properties (base URLs, timeouts)
├── conftest.py       # Centralized Pytest fixtures and environment initialization
├── pytest.ini        # Core Pytest configuration rules and discovery markers
└── requirements.txt  # Project dependency manifest for pipeline reproduction
```

---

## Local Environment Setup & Installation

Follow these sequential steps to set up the automation workspace locally on your machine.

### Step 1: Directory Organization
1. Create a workspace folder on your local storage drive (`C:` or `D:`):
   ```powershell
   Project_Github_Jenkins_Integration
   ```
2. Inside that workspace, create the primary project folder:
   ```powershell
   Github_jenkins_project
   ```

### Step 2: Workspace Initialization
1. Open the project root folder inside your visual editor by launching a terminal context and entering:
   ```bash
   code .
   ```
2. Adjust your IDE **Workspace Trust** parameters if prompted by approving the author permissions banner via the **Trust** option to fully clear restricted environment locks.

### Step 3: Initialize Workspace
Create a folder named `Project_Github_Jenkins_Integration` in your local drive (`C:` or `D:`). Inside it, create your target project folder:
```bash
# Navigate to your working directory and open it in VS Code
cd D:\Project_Github_Jenkins_Integration\Github_jenkins_project
code .
```
*Note: Ensure you grant **Workspace Trust** if prompted by your code editor.*

### Step 4: Establish and Activate Virtual Environment
Open your editor terminal (PowerShell is recommended on Windows) and configure your isolated runtime:

* **Windows (PowerShell)**:
  ```powershell
  # If blocked by execution policy, run: Set-ExecutionPolicy RemoteSigned -Scope Process
  python -m venv .venv
  .\.venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt)**:
  ```cmd
  python -m venv .venv
  .\.venv\Scripts\activate
  ```
* **macOS / Linux**:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### Step 5: Configure Code Editor Interpreter
1. Press `Ctrl + Shift + P` to launch the VS Code Command Palette.
2. Search for and select **Python: Select Interpreter**.
3. Choose the path associated with your virtual environment: `.\.venv\Scripts\python.exe`.
4. Reload your editor environment (`Ctrl + Shift + P` -> **Developer: Reload Window**).

### Step 6: Install Framework Dependencies
With your virtual environment active `(.venv)`, execute the package installation commands:

```bash
# Upgrade pip to the latest verified version
python.exe -m pip install --upgrade pip

# Install the suite of required automation libraries
pip install pytest playwright pytest-xdist pytest-html allure-pytest pytest-rerunfailures openpyxl Faker python-slugify

# Download and install required Playwright browser binaries
playwright install
```
### 7. Verify Active Package Manifest
Review all current execution software mappings to ensure consistency across the setup:
```powershell

pip show allure-pytest
pip list
```

---

## Git and GitHub Synchronization Workflow

Use the following version control command sequence to push your local automation framework files onto your cloud repository.

```bash
# Initialize tracking in your local workspace root
git init

# Stage all project architecture blueprints and source files
git add .

# Snapshot the workspace with an explicit descriptive note
git commit -m "Added Github Jenkins Integration Project"

# Standardize the main branch naming format
git branch -M main

# Link the local workspace to the cloud remote hosting infrastructure
git remote add origin https://github.com/DurgeshYaduvanshi2026/GitHub-Jenkins-integration-project.git

# Force-push the local branches upstream to populate the target project
git push -u origin main
```

*Maintenance Note: If you ever need to purge a tracked target configuration file from the public cloud registry while safely retaining it locally on your machine, run:*
```powershell
git rm --cached <file_path>
```

---

## 🔄 Jenkins CI/CD Automation Integration

To establish automated continuous execution on every fresh codebase adjustment:
1. Ensure the `requirements.txt` manifest file reflects all local packages by executing `pip freeze > requirements.txt` or updating it manually.
2. Configure a Jenkins job target pointing cleanly to the repository remote source URL: `https://github.com/DurgeshYaduvanshi2026/GitHub-Jenkins-integration-project.git`.
3. Provision pipeline execution environments to invoke build tasks automatically using standard build step directives:
   ```bash
   pip install -r requirements.txt
   playwright install-deps chromium
   playwright install chromium
   pytest --alluredir=reports/allure-results
   ```
