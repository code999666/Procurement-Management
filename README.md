
## Procurement Management System

### Project Overview
The **Procurement Management System** is a web-based application that allows users to manage procurement requests, including adding, editing, and deleting items. It supports configuration management and provides a simulated procurement process, enabling efficient tracking and management of resources.

### Features
- **Add Procurement Requests**: Users can add procurement requests with details such as item name, supplier, cost, and description.
- **Edit Procurement Requests**: Existing procurement requests can be edited for any updates or changes.
- **Delete Procurement Requests**: Users can remove procurement requests that are no longer needed.
- **Configuration Management**: The project uses Git for version control, following GitFlow best practices.
- **Responsive UI**: The application is styled for ease of use and readability, with buttons and forms well organized.

---

### **Table of Contents**
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Project Structure](#project-structure)

---

### **Installation**

#### Step 1: Clone the Repository
Clone the project from GitHub:

```bash
git clone https://github.com/your_username/procurement-management-system.git
cd procurement-management-system
```

#### Step 2: Set up a Virtual Environment
Create and activate a virtual environment (optional but recommended):

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
Install all required dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

#### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory and configure your environment variables. Here's an example:

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

#### Step 5: Initialize the Database
To create the SQLite database and tables, run the following:

```bash
flask shell
>>> from procurement_app import db
>>> db.create_all()
>>> exit()
```

---

### **Usage**
Once the installation is complete, run the following command to start the Flask development server:

```bash
flask run
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

From here, you can add, edit, or delete procurement requests.

---

### **Configuration**

#### Git Version Control
The project uses **Git** and **GitHub** for version control. The branching strategy is based on **GitFlow**, with separate branches for:
- **Main branch**: The stable production branch.
- **Feature branches**: For adding new features.

#### Deployment Configuration
- **Environment variables** are loaded using `python-dotenv` to manage sensitive data and deployment-specific configurations.
- **Database migrations** are handled by `Flask-Migrate` to ensure smooth schema updates.

---

### **Dependencies**
This project uses the following dependencies:
- **Flask**: Web framework.
- **Flask-SQLAlchemy**: ORM for database management.
- **python-dotenv**: For loading environment variables.
- **Flask-Migrate**: For handling database migrations.

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

---

### **Project Structure**

```bash
procurement_management/
├── procurement_app.py          # Main application file
├── requirements.txt            # Python dependencies
├── .env                        # Environment configuration file
├── README.md                   # Project documentation
├── templates/                  # HTML templates
│   ├── base.html               # Base layout
│   ├── index.html              # Procurement list page
│   ├── add_procurement.html    # Form to add procurement request
│   └── edit_procurement.html   # Form to edit procurement request
├── static/                     # Static files (CSS, JS)
│   └── styles.css              # CSS styles
├── docs/                       # Documentation files
│   ├── procurement_rfp.md      # Procurement requirements document
│   └── project_report.md       # Configuration management and procurement report
└── procurement.db              # SQLite database file
```
