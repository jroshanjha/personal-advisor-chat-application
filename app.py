import streamlit as st
import mysql.connector
import bcrypt
from modular import learningflatform
from modular import travel
from modular import finance
from modular import medical
from modular import sentiment_analysis
import os
import logged
from logged import setup_logger
logger = setup_logger()
import logging
console = logging.StreamHandler()
console.setLevel(logging.ERROR)

logging.getLogger('').addHandler(console)
# from pages.home import index
# from pages.about import about

# MySQL Connection Configuration :- begin configuration:-
db_config = {
    "host": "127.0.0.1",
    "user": "root",  # Replace with your MySQL username
    "password": "jroshan@98",  # Replace with your MySQL password
    "database": "learning_model", # Replace with your MySQL database name
    "port":3306
}
# MySQL Connection Configuration :- end configuration:-
# conn = mysql.connector.connect(
#     host="db4free.net",
#     user="yourusername",
#     password="yourpassword",
#     database="yourdbname"
# )

# Host: sql12.freesqldatabase.com
# Database name: sql12774097
# Database user: sql12774097
# Database password: WjSWZv19Pg
# Port number: 3306
# MySQL Connection Configuration :- begin configuration:-

# --( https://phpmyadmin.co/server_sql.php?db= )
# db_config = {
#     "host":"sql12.freesqldatabase.com",
#     "user":"sql12774097",
#     "password":"WjSWZv19Pg",
#     "database":"sql12774097",
#     "port":3306
# }

# db_config = {
#     'host': os.getenv('9TNMY74'),
#     'user': os.getenv('root'),
#     'password': os.getenv('jroshan@98'),
#     'database': os.getenv('learning_model'),
#     'port': 3306,
# }

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**db_config)
# Hash Password
def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
# Check Password
def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))
# Add New User
def register_user(username, password):
    hashed = hash_password(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        # Check if the username already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = %s", (username,))
        user_exists = cursor.fetchone()[0]

        if user_exists > 0:
            st.error("Username already exists. Please choose a different username.")
        else:
            # Insert the new user
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed.decode("utf-8"))
            )
            conn.commit()
            st.success("Registration successful! Please login.")

    except mysql.connector.Error as err:
        logger.info("Authorization failed.")
        st.error(f"Error: {err}")
    finally:
        logger.info("Authorization successful.")
        cursor.close()
        conn.close()

# Authenticate User
def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password(password, user[0]):
            return True
        return False
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
# Login Form
def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.authenticated = True
            st.session_state.username = username
            st.session_state.page = "Dashboard"
            logger.info("Authorization successful.")
            st.success("Logged in successfully!")
            st.rerun()
            #st.home()
            #learningflatform.dashboard()
            #home()
        else:
            logger.info("Authorization successful.")
            st.error("Invalid username or password.")          
# Register Form
def register():
    st.title("Register")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    if st.button("Register"):
        register_user(username, password)
        #st.session_state.page = "Login"
        #st.rerun()
    # if st.button("Back to Login"):
    #     st.session_state.page = "Login"
    #     st.rerun()
# Logout section 
def logout():
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.success("Logout successful!")
        #login()
        st.session_state.page = "Login"
        st.rerun()
        #st.session_state.page = "Login"
        # if "authenticated" not in st.session_state:
        #     navigation()
        #st.session_state.authenticated = False      
# Dashboard
def leaning():
    st.title("Dashboard")
    st.write(f"Welcome, {st.session_state.username}!")
    #st.dashboard()
    learningflatform.dashboard()   
    #learningflatform()
    
# Navigation
def navigation():
    if "page" not in st.session_state:
        st.session_state.page = "Login"

    pages = {
        # "Home": home,
        # "About": about,
        "Login": login,
        "Register": register,
        "Learning Platform": leaning,
        "Smart Travel Planner": travel.t_ravel,
        "Personal Finance Advisor":finance.financial,
        "Medical Diagnostic":medical.medical_method,
        "Text-Analysis":sentiment_analysis.main,
        "Logout":logout,
    }
    st.set_page_config("Welcome AI Chatbot Application")
    # Sidebar for Navigation
    with st.sidebar:
        st.title("Navigation")
        if st.session_state.authenticated:
            selection = st.radio("Go to", ["Learning Platform","Smart Travel Planner","Personal Finance Advisor","Medical Diagnostic","Text-Analysis","Logout"])
        else:
            selection = st.radio("Go to", ["Login", "Register"]) # "Home", "About"

        st.session_state.page = selection

    # Render the selected page
    pages[st.session_state.page]()

# # Main Application Logic
# if st.session_state.authenticated:
#     learningflatform.dashboard()
# else:
#     menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
#     if menu == "Login":
#         login()
#     elif menu == "Register":
#         register()

# # Streamlit Session State Management
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
    st.session_state.username = None

# Main
if __name__ == "__main__":
    logger.info("Running the main function.")
    if "authenticated" not in st.session_state and not st.session_state.username:
        st.session_state.authenticated = False
        login()
        st.rerun()
    else:
        navigation()
        
    # Footer section
    st.markdown("---")
    st.markdown("© 2024-2025 My AI Chatbot Application | All rights reserved. Developed by jroshan")

## st.sidebar.selectbox("Menu", ["Login", "Register"])