from datetime import date
import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai
import mysql.connector
import matplotlib.pyplot as plt

load_dotenv()
## configure the api key:-
genai.configure(api_key=os.getenv("GOOGLE_API_SERVICE"))
model = genai.GenerativeModel("gemini-pro")

# MySQL Connection Configuration :- begin configuration:-
db_config = {
    "host": "localhost",
    "user": "root",  # Replace with your MySQL username
    "password": "jroshan@98",  # Replace with your MySQL password
    "database": "learning_model"  # Replace with your MySQL database name
}

# connect Mysql:-
def get_db_conn():
    #return mysql.connector.connect(**db_config)
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jroshan@98",
        database="learning_model"
    )
def get_gemini_response(text):
    response = model.generate_content(text)
    return response.text

def log_progress(user_id, lesson_name, score):
    try:
        conn = get_db_conn()
        cursor = conn.cursor()
        #cursor.execute("use learning_model")
        cursor.execute("""
            INSERT INTO progress (user_id, lesson_name, score)
            VALUES (%s, %s, %s)
        """, (user_id, lesson_name, score))
        conn.commit()
        st.success("User Log Progress successfully!")
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
        return True

def fetch_user_progress(user_id):
    # conn = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="jroshan@98",
    #     database="learning_model"
    # )
    # cursor = conn.cursor()
    conn = get_db_conn()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT lesson_name, score, timestamp
        FROM progress
        WHERE user_id = %s
        ORDER BY timestamp DESC
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return pd.DataFrame(rows, columns=["Lesson", "Score", "Timestamp"])

def plot_progress(dataframe):
    # Create a figure with 2 rows and 3 columns
    #fig, axes = plt.subplots(5, 1, figsize=(30, 30))  # 5 rows, 1 columns

    # Line Plot
    fig1 = plt.figure(figsize=(10, 5))
    plt.plot(dataframe["Lesson"], dataframe["Score"], marker="o", color="b")
    plt.title("Line Plot - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig1)

    # Bar Chart
    fig2 = plt.figure(figsize=(10, 5))
    plt.bar(dataframe["Lesson"], dataframe["Score"], color="skyblue")
    plt.title("Bar Chart - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Histogram
    fig3 = plt.figure(figsize=(10, 5))
    plt.hist(dataframe["Score"], bins=5, color="orange", edgecolor="black")
    plt.title("Histogram - Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    st.pyplot(fig3)

    # Pie Chart
    fig4 = plt.figure(figsize=(10, 5))
    plt.pie(
        dataframe["Score"], 
        labels=dataframe["Lesson"], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=plt.cm.Paired.colors
    )
    plt.title("Pie Chart - Score Distribution")
    st.pyplot(fig4)

    # Scatter Plot
    fig5 = plt.figure(figsize=(10, 5))
    plt.scatter(dataframe["Lesson"], dataframe["Score"], color="green", alpha=0.7)
    plt.title("Scatter Plot - User Progress")
    plt.xlabel("Lesson")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    st.pyplot(fig5)
    

def dashboard():
    #st.set_page_config("AI-Powered Learning Platform 📚")
    # App Title
    st.title("Welcome to AI-Powered Learning Platform 📚")
    # Sidebar Menu
    menu = st.sidebar.radio("Menu", ["Personalized Lessons", "Practice Exercises", "AI Tutor","Flash Card" ,"Lesson Recommendations","Progress Tracker"])
    
    prompt = "Tell me about Learning Platform"
    
    if menu == "Personalized Lessons":
        st.header("Generate Personalized Lessons")
        subject = st.text_input("Enter Subject (e.g., Python, Calculus, History)")
        level = st.selectbox("Select Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
        goal = st.text_area("What would you like to learn?")

        if st.button("Generate Lesson"):
            prompt = f"Create a detailed lesson on {subject} at a {level} level. Learning goal: {goal}."
            st.write("### Lesson Content:")

    elif menu == "Practice Exercises":
        st.header("Practice Exercises")
        topic = st.text_input("Enter Topic (e.g., Python Loops, Calculus Derivatives)")
        num_questions = st.slider("Number of Questions", 1, 20, 5)
        if st.button("Generate Exercises"):
            result = log_progress(101,topic,8)
            # if result ==True:
            #     pass
            prompt = f"Create {num_questions} practice questions with answers on {topic}."
            st.write("### Practice Questions:")

    elif menu == "AI Tutor":
        st.header("Chat with the AI Tutor")
        question = st.text_input("Ask a question about any topic (e.g., 'Explain Newton's second law')")
        if st.button("Get Answer"):
            prompt = f"Explaine this topic in depth for interview and exam pointviews."
            st.write("### Tutor's Answer:")

    elif menu =='Flash Card':
        topic = st.text_input("Enter Topic for Flashcards")
        if st.button("Generate Flashcards"):
            prompt = f"Create top 20 flashcards with questions and answers on {topic}."
    elif menu=='Lesson Recommendations':
        c_lesson = st.text_input("Enter Your Complete Topics")
        if st.button("Recommendations Next Lesson!"):
            prompt = f"I have Completes the lesson {c_lesson} and pleased recommendations"

    #elif menu=='Progress Tracker':

    elif menu == "Progress Tracker":
        st.header("Track Your Progress")
        user_id = st.text_input("Enter User ID", "user123")
        #st.write("Feature Coming Soon: Integrate with user authentication and database to track completed lessons, scores, and improvement areas.")
        if st.button("View Progress"):
            progress_df = fetch_user_progress(user_id)
            if not progress_df.empty:
                st.write("### Progress Data:")
                st.dataframe(progress_df)
                plot_progress(progress_df)
            else:
                st.write("No progress data found!")
                
    response = get_gemini_response(prompt)
    #st.subheader('The response Output:-')
    st.write(response)
    
    
# Main
if __name__ == "__main__":
    dashboard()