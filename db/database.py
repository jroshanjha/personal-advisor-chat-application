# from flask import Flask, render_template, request, redirect, flash
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# password = "jroshan@98"
# # ✅ MySQL DB Configuration
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{{password}}@localhost/learning_model'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # ✅ DB Model
# class Subscriber(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)

# # ✅ Create table
# with app.app_context():
#     db.create_all()

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         if email:
#             if not Subscriber.query.filter_by(email=email).first():
#                 new_subscriber = Subscriber(email=email)
#                 db.session.add(new_subscriber)
#                 db.session.commit()
#                 flash("Successfully subscribed!", "success")
#             else:
#                 flash("Email already subscribed.", "warning")
#         else:
#             flash("Please enter a valid email.", "danger")
#         return redirect('/')
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)


import streamlit as st
import mysql.connector

# ✅ Set up MySQL connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jroshan@98",
        database="learning_model"
    )

# ✅ Create table if not exists
def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ✅ Insert email into DB
def insert_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        conn.close()

# ✅ Initialize table
create_table()

# ✅ Streamlit UI
# st.title("📧 Subscribe to Our Newsletter")

# email = st.text_input("Enter your email")

# if st.button("Subscribe"):
#     if email:
#         if insert_email(email):
#             st.success("✅ Successfully subscribed!")
#         else:
#             st.warning("⚠️ Email already subscribed.")
#     else:
#         st.error("❌ Please enter a valid email.")
