import streamlit as st
import mysql.connector
import bcrypt

# from app1 import app as app1
#from learningflatform import learningflatform as app1
import learningflatform
from travel import t_ravel
from finance import financial
from medical import medical_method
# import travel
# import finance
from pages.home import home
from pages.about import about

# MySQL Connection Configuration :- begin configuration:-
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "jroshan@98",  # Replace with your MySQL password
    "database": "learning_model"  # Replace with your MySQL database name
}

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
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed.decode("utf-8")))
        conn.commit()
        st.success("User registered successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
# Authenticate User
def authenticate_user(username, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        if user and check_password(password, user[0]):
            return True
        return False
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
            st.success("Login successful!")
            #st.home()
            learningflatform.dashboard()
            #home()
            
        else:
            st.error("Invalid username or password.")
    # Footer section
    # st.markdown("---")
    # st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")
# Register Form
def register():
    st.title("Register")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    if st.button("Register"):
        register_user(username, password)
    
    # Footer section
    st.markdown("---")
    st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")

# Logout section 
def logout():
    if st.button("Logout"):
        st.session_state.authenticated = False
        st.session_state.username = None
        st.success("Logout successful!")
        login()
        #st.session_state.page = "Login"
        # if "authenticated" not in st.session_state:
        #     navigation()
        #st.session_state.authenticated = False
    
        
    # Footer section
    st.markdown("---")
    st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")
        
# Dashboard
def leaning():
    st.title("Dashboard")
    st.write(f"Welcome, {st.session_state.username}!")
    #st.dashboard()
    learningflatform.dashboard()
    
    # Footer section
    st.markdown("---")
    st.markdown("© 2024 My Chat Application | All rights reserved. Develop by jroshan")
    
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
        "Smart Travel Planner": t_ravel,
        "Personal Finance Advisor":financial,
        "Medical Diagnostic":medical_method,
        "Logout":logout,
    }

    # Sidebar for Navigation
    with st.sidebar:
        st.title("Navigation")
        if st.session_state.authenticated:
            selection = st.radio("Go to", ["Learning Platform","Smart Travel Planner","Personal Finance Advisor","Medical Diagnostic","Logout"])
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

# Main
if __name__ == "__main__":
    if "authenticated" not in st.session_state and st.session_state.username:
        st.session_state.authenticated = False
    navigation()