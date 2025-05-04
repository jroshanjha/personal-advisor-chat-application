# pip install mysql-connector-python
import streamlit as st
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Database Initialization
# MySQL Connection Configuration
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="jroshan@98"
)

# conn = mysql.connector.connect(
#     host="sql12.freesqldatabase.com",
#     user="sql12774097",
#     password="WjSWZv19Pg"
# )
cursor = conn.cursor()


# Creating a new database or Table
#cursor.execute("CREATE DATABASE IF NOT EXISTS learning_model")
#print("Database 'learning_model' created successfully!")
def init_db():
    conn = mysql.connector.connect(
        host="sql12.freesqldatabase.com",
        user="sql12774097",
        password="WjSWZv19Pg",
        database=" sql12774097" # learning_model
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS progress (
            user_id VARCHAR(255),
            lesson_name VARCHAR(255),
            score INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


""" ################## CREATE TABLE IF NOT EXISTS ################### """
def create_database_and_table():
    try:
        # Use the new database
        cursor.execute("USE sql12774097")
        # Create Table
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS progress (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id VARCHAR(255) NOT NULL,
                    lesson_name VARCHAR(255) NOT NULL,
                    score INT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        cursor.execute("""
                       CREATE TABLE if not exists users (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(255) NOT NULL UNIQUE,
                                password VARCHAR(255) NOT NULL,
                                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                            )
                       """)
        print("Table 'progress' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            pass
            # cursor.close()
            # conn.close()
# # Run the function to create the database and table
#create_database_and_table()


"""...............................................................
################### DB TABLE INSERT VALUE:-#######################
..............................................................."""
# Default Data (Top 20 Progress Records)
default_values = [
    {"user_id": f"user_{i+101}", "lesson_name": f"Lesson_{i+101}", "score": (i + 1) * 10}
    for i in range(50)
]
# Custom Default Data (Update as Needed)
default_values = [
    {"user_id": "admin_user", "lesson_name": "Introduction", "score": 89},
    {"user_id": "guest_user", "lesson_name": "Basics of Python", "score": 80},
    {"user_id": "user_1", "lesson_name": "Advanced SQL", "score": 84},
    {"user_id": "user_2", "lesson_name": "Web Development", "score": 89},
    {"user_id": "jroshan", "lesson_name": "Data Science", "score": 76},
    {"user_id": "programmer123", "lesson_name": "Python Advanced", "score": 58},
    {"user_id": "user_1", "lesson_name": "Advanced SQL", "score": 45},
    {"user_id": "user_2", "lesson_name": "Frontend", "score": 690},
    {"user_id": "system_admin", "lesson_name": "Networking", "score": 79},
    {"user_id": "tution98", "lesson_name": "Basics of Python", "score": 70},
    {"user_id": "user_1", "lesson_name": "Advanced SQL", "score": 95},
    {"user_id": "user_2", "lesson_name": "Backend", "score": 90},
    # Add up to 20 or more custom entries here as needed
]
# SELECT * FROM progress LIMIT 20;
def insert_default_values():
    try:
        # Connect to MySQL Server
        # conn = mysql.connector.connect(**db_config)
        # cursor = conn.cursor()
        cursor.execute("use sql12774097")
        # Insert Default Values
        for entry in default_values:
            cursor.execute("""
                INSERT INTO progress (user_id, lesson_name, score)
                VALUES (%s, %s, %s)
            """, (entry["user_id"], entry["lesson_name"], entry["score"]))

        conn.commit()
        print("Top 20 default values inserted successfully!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
# Run the function to insert default values
insert_default_values()



