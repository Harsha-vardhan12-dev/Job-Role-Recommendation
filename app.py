from flask import Flask, render_template, request, jsonify
from database import create_database, save_recommendation
from datetime import datetime

app = Flask(__name__)


# ==========================================
# JOB ROLES AND REQUIRED SKILLS
# ==========================================

JOB_ROLES = {

    "Data Analyst": {
        "skills": [
            "Python",
            "SQL",
            "Excel",
            "Power BI",
            "Statistics"
        ],
        "description":
            "Analyze data, create dashboards and generate business insights.",
        "icon": "📊"
    },

    "Web Developer": {
        "skills": [
            "HTML",
            "CSS",
            "JavaScript",
            "Git"
        ],
        "description":
            "Build modern websites and interactive web applications.",
        "icon": "🌐"
    },

    "Python Developer": {
        "skills": [
            "Python",
            "SQL",
            "Git",
            "OOP"
        ],
        "description":
            "Develop software applications and backend systems using Python.",
        "icon": "🐍"
    },

    "Cybersecurity Analyst": {
        "skills": [
            "Networking",
            "Linux",
            "Python",
            "Cybersecurity"
        ],
        "description":
            "Protect computer systems, networks and applications from threats.",
        "icon": "🔐"
    },

    "Software Developer": {
        "skills": [
            "Python",
            "Java",
            "OOP",
            "Git",
            "Problem Solving"
        ],
        "description":
            "Design, develop and maintain software applications.",
        "icon": "💻"
    },

    "Database Administrator": {
        "skills": [
            "SQL",
            "MySQL",
            "Database",
            "Linux"
        ],
        "description":
            "Manage databases, security, backups and database performance.",
        "icon": "🗄️"
    }
}


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================================
# RECOMMEND JOB ROLES
# ==========================================

@app.route("/recommend", methods=["POST"])
def recommend():

    # Get skills selected by the user
    selected_skills = request.form.getlist("skills")

    recommendations = []


    # Check each job role
    for role, details in JOB_ROLES.items():

        required_skills = details["skills"]

        # Find matching skills
        matching_skills = [
            skill
            for skill in selected_skills
            if skill in required_skills
        ]

        # Find missing skills
        missing_skills = [
            skill
            for skill in required_skills
            if skill not in selected_skills
        ]

        # Calculate match percentage
        percentage = round(
            (len(matching_skills) / len(required_skills)) * 100
        )

        recommendations.append({

            "role": role,

            "percentage": percentage,

            "matching_skills": matching_skills,

            "missing_skills": missing_skills,

            "description": details["description"],

            "icon": details["icon"]
        })


    # Sort highest match first
    recommendations.sort(
        key=lambda x: x["percentage"],
        reverse=True
    )


    # ==========================================
    # SAVE RESULT TO DATABASE
    # ==========================================

    if selected_skills and recommendations:

        best_role = recommendations[0]

        save_recommendation(

            ", ".join(selected_skills),

            best_role["role"],

            best_role["percentage"],

            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        )


    # Send results to result.html
    return render_template(

        "result.html",

        recommendations=recommendations,

        selected_skills=selected_skills
    )


# ==========================================
# API RECOMMENDATION
# ==========================================

@app.route("/api/recommend", methods=["POST"])
def api_recommend():

    data = request.get_json()

    if not data:
        return jsonify({
            "success": False,
            "message": "No data received"
        }), 400

    selected_skills = data.get("skills", [])

    recommendations = []


    # Check each role
    for role, details in JOB_ROLES.items():

        required_skills = details["skills"]

        matching_skills = [
            skill
            for skill in selected_skills
            if skill in required_skills
        ]

        missing_skills = [
            skill
            for skill in required_skills
            if skill not in selected_skills
        ]

        percentage = round(
            (len(matching_skills) / len(required_skills)) * 100
        )

        recommendations.append({

            "role": role,

            "percentage": percentage,

            "matching_skills": matching_skills,

            "missing_skills": missing_skills,

            "description": details["description"],

            "icon": details["icon"]
        })


    # Sort by percentage
    recommendations.sort(
        key=lambda x: x["percentage"],
        reverse=True
    )


    return jsonify({

        "success": True,

        "selected_skills": selected_skills,

        "recommendations": recommendations
    })


# ==========================================
# START APPLICATION
# ==========================================

if __name__ == "__main__":

    # Create database
    create_database()

    print("===================================")
    print("       CareerMatch AI")
    print(" Job Role Recommendation System")
    print("===================================")

    app.run(debug=True)