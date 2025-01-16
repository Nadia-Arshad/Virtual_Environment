# Virtual_Environment
How to set up virtual environment 

# Welcome to [Your Project Name]!

This README will guide you through setting up your development environment for this project. Let's get started!

**1. Project Setup**

* **Create a Project Folder:** 
    * Make a new folder anywhere on your machine. 
    * **Pro Tip:** Use a descriptive name for your project!

* **Open with VS Code:**
    * Right-click on the newly created folder and select "Open with VS Code."

* **Create a Virtual Environment:**
    * Open the terminal within VS Code.
    * Type: `python -m venv venv` (or choose a more descriptive name like `my_env`) 
    * This creates an isolated environment for your project's dependencies.

* **Activate the Virtual Environment:**
    * On Windows: `venv\Scripts\activate`
    * On macOS/Linux: `source venv/bin/activate` 
    * You'll see the name of your environment (e.g., `(venv)`) appear before your command prompt – you're now in your virtual environment!

**2. Project Dependencies**

* **Create a Requirements File:**
    * Run `pip freeze > requirements.txt`. This generates a file listing all the packages currently installed in your environment.

* **Install Dependencies:**
    * To install all the necessary packages for your project: `pip install -r requirements.txt`

**3. Project Configuration**

* **Create an Environment File (.env):**
    * Create a `.env` file in your project's root directory. This file will store your project's sensitive information (like API keys) securely. 
    * Example:
        ```
        API_KEY=your_actual_api_key
        ```

* **Access Environment Variables:**
    * You can access these environment variables within your Python code using libraries like `os` or `dotenv`.

**4. Let's Code!**

* Create a new Python file (e.g., `main.py`) within your project folder.
* Write your project's logic in this file, utilizing the installed dependencies and your environment variables.

Link for a detailed video: https://youtu.be/BpRdArUiYbk

**Code Example (Illustrative):**

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("API_KEY") 

# ... rest of your code ...



