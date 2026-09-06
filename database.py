import sqlite3


DATABASE_NAME = "career.db"


# ==========================================
# CREATE DATABASE
# ==========================================

def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            skills TEXT,
            recommended_role TEXT,
            match_percentage INTEGER,
            created_at TEXT
        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# SAVE RECOMMENDATION
# ==========================================

def save_recommendation(
    skills,
    recommended_role,
    match_percentage,
    created_at
):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO recommendations
        (
            skills,
            recommended_role,
            match_percentage,
            created_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        skills,
        recommended_role,
        match_percentage,
        created_at
    ))

    connection.commit()

    connection.close()