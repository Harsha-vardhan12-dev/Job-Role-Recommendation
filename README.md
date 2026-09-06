# 🎯 Job Role Recommendation System

An AI-based **Job Role Recommendation System** that recommends suitable career roles based on the skills selected by the user.

The system analyzes the user's skills, compares them with the required skills for different job roles, and displays the best matching career options with a match percentage.

## 🚀 Features

* 🎯 Skill-based job role recommendations
* 📊 Match percentage for each job role
* ✅ Displays matching skills
* ❌ Displays missing skills
* 💻 Simple and responsive web interface
* 🗄️ MySQL database integration
* 🌐 Flask backend
* 🔌 REST API endpoint for recommendations
* 📱 User-friendly interface

## 👨‍💻 Available Job Roles

The system currently recommends:

* 📊 Data Analyst
* 🌐 Web Developer
* 🐍 Python Developer
* 🔐 Cybersecurity Analyst
* 💻 Software Developer
* 🗄️ Database Administrator

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Backend programming  |
| Flask        | Web framework        |
| MySQL        | Database             |
| HTML         | Frontend structure   |
| CSS          | Styling              |
| JavaScript   | Frontend interaction |
| Git & GitHub | Version control      |

## 📁 Project Structure

```text
Job-Role-Recommendation/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    ├── style.css
    └── script.js
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Harsha-vardhan12-dev/Job-Role-Recommendation.git
```

### 2. Open the project

```bash
cd Job-Role-Recommendation
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## 🗄️ MySQL Setup

Open MySQL and create the database:

```sql
CREATE DATABASE job_recommendation;
```

Then select it:

```sql
USE job_recommendation;
```

The application will create the required `recommendations` table automatically.

## 🔐 Database Configuration

Update your `database.py` with your MySQL credentials:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "job_recommendation"
}
```

**Important:** Do not upload your real MySQL password to GitHub. Use environment variables for production.

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## 🔄 How It Works

```text
User Selects Skills
        ↓
Flask Receives Skills
        ↓
Compare With Job Requirements
        ↓
Calculate Match Percentage
        ↓
Rank Job Roles
        ↓
Display Recommendations
        ↓
Save Result in MySQL
```

## 📊 Example

If the user selects:

```text
Python
SQL
Excel
Power BI
```

The system may recommend:

```text
Data Analyst
80% Match
```

It also shows:

* ✅ Matching skills
* ❌ Missing skills
* 📊 Match percentage

## 🔌 API

The project also provides a recommendation API.

### Endpoint

```text
POST /api/recommend
```

Example request:

```json
{
    "skills": [
        "Python",
        "SQL",
        "Excel"
    ]
}
```

## 🎓 Project Purpose

This project was developed as a **BCA academic and portfolio project** to demonstrate:

* Python programming
* Flask web development
* MySQL database integration
* REST API development
* Frontend development
* Git and GitHub usage
* Basic recommendation logic

## 🔮 Future Improvements

* 🤖 Machine Learning-based recommendations
* 👤 User registration and login
* 📚 Personalized learning paths
* 📈 Career skill-gap analysis
* 💼 Job vacancy integration
* 📊 Admin dashboard
* 📄 Resume analysis
* 🧠 AI-powered career suggestions

## 👨‍💻 Author

**Harsha Vardhan**

GitHub:
https://github.com/Harsha-vardhan12-dev

---

⭐ If you find this project useful, consider giving it a star!

