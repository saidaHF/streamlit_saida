# Streamlit Saida

Welcome to **Streamlit Saida**! This is a simple Streamlit application to create my profile 🧙🏻‍♀️

## 🚀 Getting Started

Follow these steps to set up and run the project.

### 1️⃣ Prerequisites

Make sure you have Python installed on your system. You can check by running:

```powershell
python --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Create and Activate a Virtual Environment

First, create a virtual environment:

```powershell
python -m venv myenv
```

Then, activate it:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
myenv\Scripts\Activate.ps1
```

For desactivate the environment execute:
```
deactivate.bat
```

### 3️⃣ Install Dependencies

Once the virtual environment is activated, install the required dependencies:

```powershell
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

To start the Streamlit app, run:

```powershell
streamlit run .streamlit\streamlit_app.py
```

## 📌 Additional Notes

- If you encounter execution policy issues, ensure PowerShell allows script execution.
- Keep your `requirements.txt` updated by running:
  ```powershell
  pip freeze > requirements.txt
  ```

## 📄 License

This project is licensed under the MIT License.

---

You have a good day! 🎉
